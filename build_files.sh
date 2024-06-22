echo "buildin project"
python3 -m pip install -r requirements.txt

echo "migrate project"
python3 manage.py makemigrations --noinput
python3 manage.py migrate --noinput

echo "migrate static"
python3 manage.py collectstatic --noinput