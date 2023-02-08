
# Yatube API

The yatube project API was created to entertain various applications and services with Yatube. The interface allows you to perform all possible actions with posts, comments and subscriptions. To use, you need to register on the Yatube website.
## Run Locally

At the first start, for the project to function, it is necessary to install a virtual environment and perform migrations:

    $ python -m venv venv
    $ source venv/Scripts/activate
    $ pip install -r requirements.txt
    $ python yatube_api/manage.py makemigrations
    $ python yatube_api/manage.py migrate

Create superuser for admin panel:

    $ python yatube_api/manage.py createsuperuser

Run server:

    $ python yatube_api/manage.py runserver
    

After launch, the admin panel will be available at http://127.0.0.1:8000/admin/

## API Reference

#### Get auth token

```http
  POST api/v1/api-token-auth/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `username` | `string` | **Required**. Your superuser name |
| `password` | `string` | **Required**. Your superuser password |

#### Get posts:

```http
  GET, POST, PUT, PATCH, DELETE /api/v1/posts/
  GET, POST, PUT, PATCH, DELETE /api/v1/posts/$id/
```

| Headers | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `Authorization`      | `string` | Token <YOUR_TOKEN> |

#### Get groups:

```http
  GET, POST, PUT, PATCH, DELETE /api/v1/groups/
  GET, POST, PUT, PATCH, DELETE /api/v1/groups/$id/
```

| Headers | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `Authorization`      | `string` | Token <YOUR_TOKEN> |

