## Instalar com o pip
```
> pip install black (Formata mas caso nao tenha erro de sintax)
> pip install flake8 (Linter)
```

# Ativando formatação ao salvar no VSCode
1. [CRTL] + [SHIFT] + P
2. user settings
3. abrir settings.json
4. Adicionar:
```json
"[python]": {
        "editor.formatOnSave": true
    },
```