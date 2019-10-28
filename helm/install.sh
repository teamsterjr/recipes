helm upgrade --install front-end front-end
for meal in breakfast lunch dinner; do helm upgrade --install $meal recipe -f recipe/$meal/values.yaml;done
helm upgrade --install dinner-v2 recipe -f recipe/dinner/values.yaml --set recipe=dinner/dinner2.json,AppVersion=v2
