# --- Variables ---
# Nome do binário/aplicação. Mude para o nome do seu executável.
APP_NAME := myapp
# Diretório onde o binário compilado será colocado
BUILD_DIR := bin
# Flags de otimização para o compilador Go
GO_BUILD_FLAGS := -ldflags="-s -w"

# --- Targets Principais ---

.PHONY: all help build run test clean setup docker-compose-up docker-compose-down

# Alvo padrão: Mostra a mensagem de ajuda
all: help


help: ## help: Mostra esta mensagem de ajuda. Este é o alvo padrão.
	@echo "Usage: make <target>"
	@echo ""
	@echo "Alvos Comuns (Recipes):"
	
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2}'


setup: ## setup: Baixa dependências do Go e instala dependências do Python.
	@echo "--> Baixando módulos Go..."
	go mod download
	@echo "--> Instalando dependências Python (requer 'requirements.txt')..."
	pip install -r requirements.txt || true # '|| true' para ignorar erro se o arquivo não existir


build: ## build: Compila a aplicação Go.
	@echo "--> Construindo $(APP_NAME) em $(BUILD_DIR)/..."
	@mkdir -p $(BUILD_DIR)
	go build $(GO_BUILD_FLAGS) -o $(BUILD_DIR)/$(APP_NAME) ./main.go


run: build ## run: Constrói (build) e executa a aplicação.
	@echo "--> Executando $(APP_NAME)..."
	@./$(BUILD_DIR)/$(APP_NAME)


test: ## test: Executa todos os testes unitários do Go.
	@echo "--> Executando testes Go..."
	go test -v ./...

docker-compose-up: ## run the composes
	@echo "--> Subindo aplicações"
	sudo docker compose  -f python-service/compose.yaml up -d 
	sudo docker compose  -f go-service/compose.yaml up  -d 

docker-compose-down: ## remove de aplications
	@echo "--> Derrubando aplicações"
	sudo docker compose  -f python-service/compose.yaml down
	sudo docker compose  -f go-service/compose.yaml down

clean: ## clean: Remove artefatos de build, binários e caches.
	@echo "--> Limpando binários e caches..."
	@rm -rf $(BUILD_DIR)
	@go clean -cache -modcache
	@echo "Limpeza completa."
