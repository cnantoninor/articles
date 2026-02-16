PYTHON_VERSION := 3.13
VENV           := .venv
PY             := $(VENV)/bin/python
PIP            := $(VENV)/bin/pip

.PHONY: install pre-push-check install-pre-push-check

# --- 1. Create venv and install deps ---
install:
	python$(PYTHON_VERSION) -m venv $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

# --- 2. The shared check logic (DRY) ---
pre-push-check:
	bash .ai/sync-rules.sh
	$(PY) scripts/refresh-frontmatter.py topics/ templates/
	@if [ -n "$$(git diff --name-only)" ]; then \
		echo "Frontmatter was out of date and has been refreshed."; \
		echo "Review changes, commit, and push again."; \
		exit 1; \
	fi
	$(PY) scripts/validate-frontmatter.py topics/ templates/

# --- 3. Install git hook that calls the shared target ---
install-pre-push-check:
	@printf '#!/bin/bash\nset -e\nmake pre-push-check\n' > .git/hooks/pre-push
	@chmod +x .git/hooks/pre-push
	@echo "Pre-push hook installed at .git/hooks/pre-push"
