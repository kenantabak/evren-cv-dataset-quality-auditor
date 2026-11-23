# EVREN CV Dataset Quality Auditor (`evren-cv-dataset-quality-auditor`)

Production data-engineering toolkit used to audit, sanitize, and maintain **342 Grade-A open Turkish Computer Vision datasets (3.369.548 images · 31.801.667 annotations)** and **140 PRODUCTION YOLO26 / YOLO11 models** on [EVREN (`evren.ssyz.org.tr`)](https://evren.ssyz.org.tr/users/u19979974710e) and [Hugging Face (`huggingface.co/kenantabak`)](https://huggingface.co/kenantabak).

## Key Engineering Features

1. **`Errno 36` Filename Sanitizer (`sanitize_filename`)**: Deterministic SHA-256 truncation for Roboflow / open-source filenames exceeding the 255-byte Linux `ext4` limit.
2. **Validation Zero-Instance Class Filter (`select_nonempty_val_classes`)**: Automatically generates `selected_class_ids` before YOLO26 / YOLO11 training so classes with `0` validation boxes do not penalize macro `mAP@50`.
3. **Bounding-Box Geometry Auditor (`audit_yolo_boxes`)**: Flags out-of-bounds coordinates, sub-pixel noise boxes, and extreme aspect-ratio outliers.
4. **Health Score Calculator (`compute_health_score`)**: Computes 0–100 dataset health scores (`Grade A`).

## Quickstart

```bash
pip install -e .
pytest -q
evren-audit --labeled-ratio 1.0 --unique-ratio 1.0 --valid-box-ratio 0.99
```

## Links

- **EVREN Profile:** [Kenan Tabak (`@u19979974710e`)](https://evren.ssyz.org.tr/users/u19979974710e)
- **Hugging Face Hub (19 Models · 10 Dataset Suites · 4 Spaces):** [huggingface.co/kenantabak](https://huggingface.co/kenantabak)

---

### 🔗 EVREN Open-Source Ecosystem
- **EVREN Platform:** [evren.ssyz.org.tr/users/u19979974710e](https://evren.ssyz.org.tr/users/u19979974710e) (`342` Grade-A Datasets · `185` Models)
- **Live Browser ONNX Demo Space:** [EVREN-Live-Object-Detection-Demo](https://huggingface.co/spaces/kenantabak/EVREN-Live-Object-Detection-Demo)
- **Hugging Face Portfolio:** [huggingface.co/kenantabak](https://huggingface.co/kenantabak) (`19` Production Models · `10` Datasets · `4` Spaces)
- **GitHub:** [github.com/kenantabak](https://github.com/kenantabak)
- **Dev.to Technical Series:** [dev.to/kenantabak](https://dev.to/kenantabak)
