# Load packages (Load virtualenv or pip install reqs)
source ~/.pyenv/versions/ecg_app/bin/activate  # Virtualenv
# pip install -r requirements.txt  # Requirments

# Build UI
pyside2-uic resources/user_interface/mainwindow.ui -o resources/user_interface/mainwindow.py
pyside2-rcc resources/graphics/icons.qrc -o icons_rc.py

# Create requirements
pip freeze > requirements.txt

# Build file (pyinstaller)
pyinstaller --specpath "pyinstaller" \
    --workpath "pyinstaller/build" \
    --distpath "pyinstaller/dist" \
    --log-level=WARN \
    --add-data="../resources/graphics:resources/graphics" \
    --add-data="../resources/model_pretrained:resources/model_pretrained" \
    --add-data="../resources/model_finetune:resources/model_finetune" \
    --add-data="../resources/model_new:resources/model_new" \
    --windowed \
    --noconfirm \
    ecg_app.py