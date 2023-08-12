# Blogging Platform API

Welcome to the Blogging Platform API documentation!

## Installation and Setup

1. Clone the repository: `git clone https://github.com/yourusername/blogging-platform.git`
2. Install dependencies using pipenv: `pipenv install`
3. Activate the virtual environment: `pipenv shell`
4. Apply migrations: `python manage.py migrate`
5. Create a superuser for admin access: `python manage.py createsuperuser`
6. Start the development server: `python manage.py runserver`
   **optional**
7. After registering some users, run the command `python manage.py populate_dummy_data` to seed your database

## API Endpoints

### User Registration and Token Generation

#### Register a New User

**URL:** `/register/`

**Method:** `POST`

**Request:**

```json
{
	"username": "your_username",
	"email": "your_email@example.com",
	"password": "your_password"
}
```

**Response:**

```json
{
	"user": {
		"username": "your_username",
		"email": "your_email@example.com"
	},
	"token": "your_token"
}
```

#### Obtain an Authentication Token

**URL:** `/token/`

**Method:** `POST`

**Request:**

```json
{
	"username": "your_username",
	"password": "your_password"
}
```

**Responce:**

```json
{
	"token": "your_token"
}
```

### Blog Post Management

**List Blog Posts**
**URL:** `/blogs/`

**Method:** ` GET`
**response:**

```json
[
	{
		"id": 1,
		"title": "Sample Blog Post 1",
		"content": "Lorem ipsum dolor sit amet...",
		"author": "author_username",
		"created_at": "2023-08-15T12:00:00Z"
	}
]
```

#### Create a New Blog Post

**URL:** `/blogs/`

**Method:** `POST`
**Request:**

```json
{
	"title": "New Blog Post",
	"content": "This is the content of the blog post."
}
```

**Response:**

```json
{
	"id": 2,
	"title": "New Blog Post",
	"content": "This is the content of the blog post.",
	"author": "your_username",
	"created_at": "2023-08-15T13:30:00Z"
}
```

#### Retrieve, Update, and Delete Blog Post

**URL:** `/blogs/{blog_id}/`

**Method:** `GET, PUT, DELETE`
**Response `(GET)`:**

```json
{
	"id": 1,
	"title": "Sample Blog Post 1",
	"content": "Lorem ipsum dolor sit amet...",
	"author": "author_username",
	"created_at": "2023-08-15T12:00:00Z"
}
```

Request (PUT):
**Request `(PUT`:**

```json
{
	"title": "Updated Title",
	"content": "This is the updated content."
}
```

**Response `(PUT and DELETE)`:**

```json
{
	"message": "Blog post updated/deleted successfully."
}
```

## Authentication and Authorization

<h1>
Include the token in the Authorization header with the format Token your_token.
</h1>

## Models

### Tag Model

**Represents a tag that can be associated with blog posts.**

- **Fields:**
  - `name`: The name of the tag.

### Blog Model

**Represents a blog post.**

- **Fields:**
  - `title`: The title of the blog post.
  - `content`: The content of the blog post.
  - `author`: The author of the blog post (foreign key to User model).
  - `created_at`: The timestamp of when the blog post was created.
  - `tags`: Many-to-many relationship with Tag model to associate tags with the blog post.

## Views

### RegisterView

Endpoint for user registration. Allows users to register with a username, email, and password.

### BlogsView

ModelViewSet for blog post management. Provides CRUD operations for blog posts. Requires authentication.

List Blog Posts
Lists all available blog posts.

Create a New Blog Post
Creates a new blog post. Requires title and content fields.

Retrieve, Update, and Delete Blog Post
Retrieves, updates, or deletes a specific blog post using the blog_id parameter. Requires appropriate permissions.

## Pagination and Filtering

Add the page query parameter to paginate through results. Add the `search` query parameter to filter results.

## Additional Details

- Token-based Authentication: Use the token obtained from the `/token/` endpoint for API authentication. Include the token in the `Authorization` header with the format `Token your_token`.

- Permissions: Blog posts can only be updated or deleted by their author or a superuser. Other users can view blog posts.

- Pagination and Filtering: Use the `page` query parameter to paginate through results. Use the `search` query parameter to filter blog posts based on title, author, or content.

- Project Customization: Customize the project by extending the models, views, and serializers as needed.

- Error Handling: The API returns appropriate status codes and error messages for various scenarios.

- Deployment: Consider deploying the project on a production server with proper security measures.
