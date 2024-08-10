# Databricks notebook source
# MAGIC %sh
# MAGIC curl --netrc -X PATCH \
# MAGIC https://dbc-1df0e747-a842.cloud/api/2.1/accounts/316c9a18-66e9-47c4-8583-06591850d397/scim/v2/Groups/603056805956253 \
# MAGIC --header 'Content-type: application/scim+json' \
# MAGIC --data @update-group.json \
# MAGIC | jq .
# MAGIC
