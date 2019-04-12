Basic GraphQL API
-----

Basic GraphQL API with authentication support, migration support, and automatic deployment to AWS.

## Development

Requirements:
- docker
- docker-compose
- pipenv

Commands:
- `dev/initialize` Initial dependency installation, migration + seed of environment
- `dev/seed` Seed the environment with the default data set
- `dev/migrations upgrade head` Migrates schema to head of schema revisions
- `dev/migrations revision --autogenerate --message <this_is_your_migration_name>` Creates a new revision containing the diff between model and actual schema in db
- `dev/log <service>` Logs all container output tailed
- `dev/test [watch]` Run the test suite (optionally in watch mode), requires running dev/initialize for the test connection with `DB_CONNECTION=test REDIS_DB=1 dev/initialize`

GraphQL Request Flow:
request -> route -> request handler -> mutation/query -> handler -> service -> db