python ./scripts/run_benchmark.py --config-path "rolling_forecast_config.json" --data-name-list "METR-LA.csv" --strategy-args '{"horizon":96}' --model-name "time_series_library.Crossformer" --model-hyper-params '{"d_ff": 512, "d_model": 256, "horizon": 96, "seq_len": 96}' --adapter "transformer_adapter"  --gpus 0  --num-workers 1  --timeout 60000  --save-path "METR-LA/Crossformer"

python ./scripts/run_benchmark.py --config-path "rolling_forecast_config.json" --data-name-list "METR-LA.csv" --strategy-args '{"horizon":192}' --model-name "time_series_library.Crossformer" --model-hyper-params '{"d_ff": 128, "d_model": 64, "dropout": 0.2, "e_layers": 3, "factor": 10, "lr": 0.001, "n_headers": 2, "num_epochs": 20, "horizon": 192, "seg_len": 24, "seq_len": 336}' --adapter "transformer_adapter"  --gpus 0  --num-workers 1  --timeout 60000  --save-path "METR-LA/Crossformer"

python ./scripts/run_benchmark.py --config-path "rolling_forecast_config.json" --data-name-list "METR-LA.csv" --strategy-args '{"horizon":336}' --model-name "time_series_library.Crossformer" --model-hyper-params '{"d_ff": 512, "d_model": 256, "horizon": 336, "seq_len": 96}' --adapter "transformer_adapter"  --gpus 0  --num-workers 1  --timeout 60000  --save-path "METR-LA/Crossformer"

python ./scripts/run_benchmark.py --config-path "rolling_forecast_config.json" --data-name-list "METR-LA.csv" --strategy-args '{"horizon":720}' --model-name "time_series_library.Crossformer" --model-hyper-params '{"d_ff": 512, "d_model": 256, "horizon": 720, "seq_len": 96}' --adapter "transformer_adapter"  --gpus 0  --num-workers 1  --timeout 60000  --save-path "METR-LA/Crossformer"
