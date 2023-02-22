if [[ -z "$1" ]]; then
    echo "Usage: compress <folder-path>"
    exit 0
fi

FOLDER_PATH=$1
ARCHIVE_NAME="`basename $FOLDER_PATH``date +"%s"`.tar.gz"
echo -e "\e[1;36mCompressing..."
tar -czf $ARCHIVE_NAME -C $FOLDER_PATH .
echo `du -h ./$ARCHIVE_NAME`
echo -e "\e[1;32mDone ✔"

# reset terminal colors to original
tput sgr0
