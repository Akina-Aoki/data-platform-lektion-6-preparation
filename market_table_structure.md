# Market Table Structure

| column_name              | example_value                    | type    | notes            |
| ------------------------ | -------------------------------- | ------- | ---------------- |
| job_id                   | 570e2320b1478265…                | STRING  | primary key      |
| original_id              | 30079889                         | STRING  | source system ID |
| headline                 | Matbud till Pizzeria Campino…    | STRING  | searchable       |
| description_text         | Om jobbet Som matbud…            | TEXT    | long text        |
| employer_name            | WOLF ENTERPRISES AB              | STRING  | dimension        |
| employer_org_number      | 5592507106                       | STRING  | business key     |
| workplace_name           | Food Partner                     | STRING  |                  |
| city                     | NORRKÖPING                       | STRING  |                  |
| region                   | Östergötlands län                | STRING  |                  |
| country                  | Sverige                          | STRING  |                  |
| latitude                 | 58.58723595                      | FLOAT   |                  |
| longitude                | 16.18940919                      | FLOAT   |                  |
| occupation_label         | Budbilsförare                    | STRING  |                  |
| occupation_group         | Övriga bil-, motorcykel…         | STRING  |                  |
| occupation_field         | Transport, distribution, lager   | STRING  |                  |
| employment_type          | Vanlig anställning               | STRING  |                  |
| working_hours            | Heltid                           | STRING  |                  |
| scope_min                | 100                              | INT     | percent          |
| scope_max                | 100                              | INT     | percent          |
| remote_work              | false                            | BOOLEAN |                  |
| experience_required      | true                             | BOOLEAN |                  |
| driving_license_required | true                             | BOOLEAN |                  |
| salary_type              | Fast månads- vecko- eller timlön | STRING  |                  |
| number_of_vacancies      | 2                                | INT     |                  |
| publication_date         | 2025-09-29                       | DATE    |                  |
| application_deadline     | 2025-10-28                       | DATE    |                  |
| detected_language        | sv                               | STRING  |                  |
| timestamp_ingested       | 1759096990839                    | BIGINT  | lineage          |
