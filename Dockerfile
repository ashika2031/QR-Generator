FROM python:3.12-slim-bullseye
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN useradd -m myuser && mkdir qr_codes && chown myuser:myuser qr_codes
COPY --chown=myuser:myuser . .
USER myuser
ENTRYPOINT ["python", "main.py"]
CMD ["--url", "https://www.njit.edu"]
