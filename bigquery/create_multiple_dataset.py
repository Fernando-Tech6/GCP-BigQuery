# Será criado multiplos datasets, utilizando um laço for para criar o final dos nomes
# e outro for para interar a variavel


from google.cloud import bigquery

# Construct a BigQuery client object.
client = bigquery.Client()

# Gerar números aleatorios para compor o nome do dataset, pois o BQ não permite nomes repetidos
for x in range(3):
    # TODO(developer): Set dataset_id to the ID of the dataset to create.
    # Colocar o nome do dataset
    dataset_id = "{}.dataset_teste_{}".format(client.project, x)

    # Construct a full Dataset object to send to the API.
    dataset = bigquery.Dataset(dataset_id)

    # TODO(developer): Specify the geographic location where the dataset should reside.
    # Localidade do servidor
    dataset.location = "southamerica-east1"

    # Make an API request.
    dataset = client.create_dataset(dataset, timeout=30)
    print("Created dataset {}.{}".format(client.project, dataset.dataset_id))
