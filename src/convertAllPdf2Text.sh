#!/bin/sh
extension=".txt"
fileName="TextFiles/"
if [ "$#" -eq  "0" ]
then
    echo "Please Give a Folder Name as arguments"
else
    j=$1;
    mkdir $fileName
    for i in $j/*.pdf
    do
        pdfname="$(echo $i | rev | cut -d "/" -f 1 | rev | cut -d "." -f 1)"
        echo $fileName$pdfname$extension
        python pdf2text.py "$i" > "$fileName$pdfname$extension"
        echo "Converting :"  $pdfname
    done
	python code.py $fileName
fi
