# Build wheel and set the $share_folder to the artifacts folder
sh $(dirname $0)/build.sh

share_folder="$(dirname $0)/../../artifacts"