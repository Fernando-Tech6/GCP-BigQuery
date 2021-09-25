# Utilizando o script que o BigQuery fornece, será completado com informações para criar um dataset
# OBS : Esse script será rodado no shell cloud da google

from google.cloud import bigquery

# Construct a BigQuery client object.
client = bigquery.Client()

# TODO(developer): Set dataset_id to the ID of the dataset to create.
# Colocar o nome do dataset
dataset_id = "{}.Nome_Do_Dataset".format(client.project)

# Construct a full Dataset object to send to the API.
dataset = bigquery.Dataset(dataset_id)

# TODO(developer): Specify the geographic location where the dataset should reside.
# Localidade do servidor
dataset.location = "southamerica-east1"

dataset = client.create_dataset(dataset, timeout=30)  # Make an API request.
print("Created dataset {}.{}".format(client.project, dataset.dataset_id))
