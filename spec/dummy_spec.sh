#shellcheck shell=sh
Describe 'queries to Zenodo API'
  cleanup() { make clean; }
  Describe 'get depositions'
    AfterAll 'cleanup'
    list_file="depositions_list.json"
    It 'create a deposition'
      file="new_deposition.json"
      When run curl -H "Content-Type: application/json" -X POST --data '{"metadata": {"title": "Intento 1", "upload_type": "dataset", "description": "This is my first upload", "access_right": "restricted", "creators": [{"name": "Ciencia de Datos", "affiliation": "GECI"}]}}' https://sandbox.zenodo.org/api/deposit/depositions?access_token=$ACCESS_TOKEN -o $file
      The stderr should include "100"
      The file $file should be exist
    End
    It 'list current depositions'
      list_file="depositions_list.json"
      When run curl -o $list_file https://sandbox.zenodo.org/api/deposit/depositions?access_token=$ACCESS_TOKEN
      The stderr should include "100"
      The file $list_file should be exist
    End
    It 'get_bucket'
      # id_new_deposition=$(jq '.[-1] | select(.id) | .id' $list_file)
    End
  End
End
