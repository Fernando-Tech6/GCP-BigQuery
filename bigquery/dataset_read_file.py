# Será criado um script para ler um arquivo externo e copiar o texto para o nome do dataset.
from google.cloud import bigquery

# Construct a BigQuery client object.
client = bigquery.Client()

# Abrir e ler o arquivo externo
with open('texto.txt', 'r') as texto:
    leitura = texto.read()
    lista = leitura.split()  # Utilizando o split para criar uma lista


for x in lista:
    # TODO(developer): Set dataset_id to the ID of the dataset to create.
    # Colocar o nome do dataset para cada interação
    # print(x)
    dataset_id = "{}.{}".format(client.project, x)

    # Construct a full Dataset object to send to the API.
    dataset = bigquery.Dataset(dataset_id)

    # TODO(developer): Specify the geographic location where the dataset should reside.
    # Localidade do servidor
    dataset.location = "southamerica-east1"

    # Make an API request.
    dataset = client.create_dataset(dataset, timeout=30)
    print("Created dataset {}.{}".format(client.project, dataset.dataset_id))
