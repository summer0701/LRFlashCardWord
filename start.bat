echo pull
git pull
echo activate
call D:\tubetoppt\venv\Scripts\activate.bat
echo retrive
D:\tubetoppt\venv\Scripts\python D:\LRFlashCardWord\LRFlashCardOrder.py
echo add
git add D:\LRFlashCardWord\.

echo "commit" 
 git commit -am '_'
echo "push" 
 git push