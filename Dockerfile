FROM python:3.11

RUN pip install --user poetry
ENV PATH="${PATH}:/root/.local/bin"

RUN mkdir /workspace
WORKDIR /workspace
# no ideal I know
COPY . ./
RUN cd backend && poetry lock && poetry install