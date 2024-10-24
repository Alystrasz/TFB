python ./scripts/run_benchmark.py --config-path "rolling_forecast_config.json" --data-name-list "NASDAQ.csv" --strategy-args '{"horizon":24}' --model-name "self_impl.VAR_model" --gpus 0  --num-workers 1  --timeout 60000  --save-path "NASDAQ/VAR"

python ./scripts/run_benchmark.py --config-path "rolling_forecast_config.json" --data-name-list "NASDAQ.csv" --strategy-args '{"horizon":36}' --model-name "self_impl.VAR_model" --gpus 0  --num-workers 1  --timeout 60000  --save-path "NASDAQ/VAR"

python ./scripts/run_benchmark.py --config-path "rolling_forecast_config.json" --data-name-list "NASDAQ.csv" --strategy-args '{"horizon":48}' --model-name "self_impl.VAR_model" --gpus 0  --num-workers 1  --timeout 60000  --save-path "NASDAQ/VAR"

python ./scripts/run_benchmark.py --config-path "rolling_forecast_config.json" --data-name-list "NASDAQ.csv" --strategy-args '{"horizon":60}' --model-name "self_impl.VAR_model" --gpus 0  --num-workers 1  --timeout 60000  --save-path "NASDAQ/VAR"
