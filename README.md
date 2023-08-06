# car_price_prediction
1. Установить docker
Airflow с помощью Docker Compose
2. Подготовка папки и окружения:
cd ~
mkdir airflow-docker
cd airflow-docker
curl -O https://airflow.apache.org/docs/apache-airflow/stable/docker-compose.yaml
mkdir ./dags ./logs ./plugins
3. Поднять airflow-init с помощью Docker Сompose:
docker-compose up airflow-init
4. Поднять Docker Compose для Airflow:
docker-compose up
5. Скопировать даг из папки со скриптами:
cp ~/airflow_hw/dags/hw_dag.py ~/airflow-docker/dags
6. Положить скрипты pipeline и predict в контейнеры worker и scheduler. Узнать ID контейнеров worker и scheduler: 
docker ps | grep worker
docker ps | grep scheduler
Положить:
docker cp ~/airflow_hw worker_id:/home/airflow/airflow_hw
docker cp ~/airflow_hw scheduler_id:/home/airflow/airflow_hw
7. Зайти в командную строку контейнеров и установите нужные для работы пайплайна/предикта пакеты (scikit-learn, dill, pandas и т.д.):
docker exec -it worker_id bash
pip install scikit-learn
8. Если при запуске пайплайна возникает ошибка при сохранении pkl-дампа модели, зайти в контейнеры worker и scheduler от имени root-пользователя и дать права командой chmod:
docker exec -it -u root container_id bash
cd /home/airflow/airflow_hw
chmod -R 777 data dags modules

