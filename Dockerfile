FROM python:3.10.9
SHELL ["/bin/bash", "-c"]

# PYTHONDONTWRITEBYTECODE: Запрещает Python записывать файлы pyc на диск (эквивалент опции python -B)
ENV PYTHONDONTWRITEBYTECODE 1
# PYTHONUNBUFFERED: Запрещает Python буферизовать stdout и stderr (эквивалент опции python -u)
ENV PYTHONUNBUFFERED 1

# Обновляем pip
RUN pip install --upgrade pip

# Доустанавливаем что нужно
RUN apt update && apt -qy install gcc libjpeg-dev libxslt-dev \
    libpq-dev libmariadb-dev libmariadb-dev-compat gettext cron openssh-client flake8 locales vim

# создаем юзера и даем права на доступ
RUN useradd -rms /bin/bash django && chmod 777 /opt /run


#создаем директорию куда все складывать
WORKDIR /django
RUN mkdir /django/media
RUN mkdir /django/media/image
RUN mkdir /django/static && mkdir /django/media/orders  && mkdir /django/media/arhive && chown -R django:django /django && chmod 755 /django

# Копируем файлы проекта
COPY --chown=django:django ../../Downloads/Banner-master/Banner-master .

# Ставим зависимости
RUN pip install -r requirements.txt

# переключаюсь на пользователя django
USER django
# Запускаю
CMD ["gunicorn","-b","0.0.0.0:8000","mysite.wsgi:application"]

