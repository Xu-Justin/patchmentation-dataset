FROM jstnxu/patchmentation:env

RUN pip --no-cache-dir install -r /requirements.txt

WORKDIR /workspace
CMD ["bash"]