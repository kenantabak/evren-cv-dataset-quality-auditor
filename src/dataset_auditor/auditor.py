import hashlib
import os
from typing import Dict, List, Set, Tuple

def sanitize_filename(filename: str, max_bytes: int = 240) -> str:
    """Prevent Linux ext4 Errno 36 (File name too long > 255 bytes) while preserving uniqueness."""
    base, ext = os.path.splitext(filename)
    encoded = filename.encode("utf-8")
    if len(encoded) <= max_bytes:
        return filename
    digest = hashlib.sha256(encoded).hexdigest()[:12]
    ext_bytes = ext.encode("utf-8")
    keep_bytes = max(32, max_bytes - len(ext_bytes) - 13)
    prefix = base.encode("utf-8")[:keep_bytes].decode("utf-8", errors="ignore")
    return f"{prefix}_{digest}{ext}"

def audit_yolo_boxes(boxes: List[Tuple[int, float, float, float, float]], min_area: float = 0.0004, max_area: float = 0.95, max_ar: float = 15.0) -> Dict[str, int]:
    """Audit normalized YOLO (cls, cx, cy, w, h) annotations for degenerate geometry."""
    stats = {"total": len(boxes), "valid": 0, "out_of_bounds": 0, "tiny_or_huge": 0, "extreme_aspect": 0}
    for _, cx, cy, w, h in boxes:
        if w <= 0 or h <= 0 or cx < 0 or cy < 0 or cx > 1 or cy > 1:
            stats["out_of_bounds"] += 1
            continue
        area = w * h
        if area < min_area or area > max_area:
            stats["tiny_or_huge"] += 1
            continue
        if max(w / h, h / w) > max_ar:
            stats["extreme_aspect"] += 1
            continue
        stats["valid"] += 1
    return stats

def select_nonempty_val_classes(train_counts: Dict[str, int], val_counts: Dict[str, int], min_val_instances: int = 1) -> List[str]:
    """Filter out classes with zero validation instances so macro mAP@50 is not diluted by empty val classes."""
    return sorted([cid for cid, t_cnt in train_counts.items() if t_cnt > 0 and val_counts.get(cid, 0) >= min_val_instances])

def compute_health_score(labeled_ratio: float, unique_ratio: float, valid_box_ratio: float, split_balanced: bool = True) -> Tuple[int, str]:
    """Compute EVREN-compatible 0-100 dataset health score and letter grade."""
    score = int(round(40 * min(1.0, labeled_ratio) + 30 * min(1.0, unique_ratio) + 20 * min(1.0, valid_box_ratio) + (10 if split_balanced else 0)))
    grade = "A" if score >= 85 else ("B" if score >= 70 else ("C" if score >= 50 else "D"))
    return score, grade
