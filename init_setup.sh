echo [$(date)]: "START"
echo [$(date)]: "Create conda environment"

conda create --prefix ./env python=3.8 -y
echo [$(date)]: "Activate environment"
source activate ./env
echo [$(date)]: "Install dev requirements"
pip install -r requirements_dev.txt
echo [$(date)]: "END"