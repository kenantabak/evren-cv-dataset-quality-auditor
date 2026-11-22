from dataset_auditor import sanitize_filename, audit_yolo_boxes, select_nonempty_val_classes, compute_health_score

def test_sanitize_filename_errno36():
    long_name = "a" * 300 + ".jpg"
    safe = sanitize_filename(long_name)
    assert len(safe.encode("utf-8")) <= 240
    assert safe.endswith(".jpg")

def test_audit_yolo_boxes():
    boxes = [(0, 0.5, 0.5, 0.2, 0.2), (1, 1.5, 0.5, 0.1, 0.1), (0, 0.5, 0.5, 0.001, 0.0001)]
    res = audit_yolo_boxes(boxes)
    assert res["valid"] == 1
    assert res["out_of_bounds"] == 1

def test_select_nonempty_val_classes():
    kept = select_nonempty_val_classes({"c1": 100, "c2": 50}, {"c1": 12, "c2": 0})
    assert kept == ["c1"]

def test_compute_health_score():
    score, grade = compute_health_score(1.0, 1.0, 1.0, True)
    assert score == 100 and grade == "A"
