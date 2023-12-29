migrations-new:
	@echo 'Creating migration files for ${name}...'
	migrate create -ext=.sql -dir=./migrations ${name}

migrations-up:
	@echo 'Running up migrations...'
	migrate -path ./migrations -database ${MUBIFY_DB_DSN} up

migrations-down:
	@echo 'Running down migrations...'
	migrate -path ./migrations -database ${MUBIFY_DB_DSN} down -all