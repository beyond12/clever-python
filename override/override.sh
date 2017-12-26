 # delete existing files
rm -rf clever || true
# Copy autogenerated files into clever directory and rename
cp -R swagger_client/. clever || true
rm -rf swagger_client || true

# Rename references of swagger client to Clever
git grep -l 'swagger_client' -- './*' ':(exclude)override/override.sh' | xargs sed -i "" 's/swagger_client/clever/g'
git grep -l 'swagger-client' -- './*' ':(exclude)override/override.sh' | xargs sed -i "" 's/swagger-client/clever-python/g'

# Update the README
mv README.md docs/README.md
sed -i "" 's/## Documentation for API Endpoints/<EOD>\'$'\n## Documentation for API Endpoints/g' docs/README.md
sed -i "" '/## Requirements./,/<EOD>/d' docs/README.md
sed -i "" '/## Author/d' docs/README.md
sed -i "" 's/docs\///g' docs/README.md
git grep -l '../README.md' -- './docs/*' | xargs sed -i "" 's/..\/README.md/README.md/g'
cp override/README.md README.md


# Copy override files for events
cp override/api_client.py clever/
cp override/*_created.py clever/models/
cp override/*_updated.py clever/models/
cp override/*_deleted.py clever/models/

# Copy other files over
cp override/VERSION clever/
cp override/version.py clever/
cp override/importer.py clever/
mkdir -p clever/data
cp override/clever.com_ca_bundle.crt clever/data/
