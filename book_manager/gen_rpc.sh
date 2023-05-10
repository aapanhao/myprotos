target_p='grpc_demo'
source_p='protos'
service_list=('book' 'user')

rm -r "${target_p:?}/${source_p:?}"*

mkdir -p "${target_p:?}/${source_p:?}"

for service in "${service_list[@]}"
do
  mkdir -p "${target_p:?}/${source_p:?}/${service:?}"
  echo "from proto file:" $source_p/"$service"/*.proto "gen proto py file to" $target_p/$source_p/"$service"
  python -m grpc_tools.protoc \
  --python_out=./$target_p \
  --grpc_python_out=./$target_p \
  -I. $source_p/"$service"/*.proto \
  --mypy_grpc_out=./$target_p \
  --mypy_out=./$target_p

  touch $target_p/$source_p/"$service"/__init__.py

  echo $target_p/$source_p/$service/*.py

  # mac 系统 sed 和 linux 不太一样
  sed -i '' "s/from protos.$service import/from . import/" $target_p/$source_p/$service/*.py
done