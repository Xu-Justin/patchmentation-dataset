FROM jstnxu/patchmentation:env

WORKDIR /workspace

COPY . .
RUN pip --no-cache-dir install -r requirements.txt

CMD ["bash"]