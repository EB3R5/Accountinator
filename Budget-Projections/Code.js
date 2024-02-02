function queryBigQueryAndWriteToSheet() {
  // Your BigQuery project and dataset information
  var projectId = 'serene-lotus-403821';
  var datasetId = 'project1';

  // Your BigQuery SQL query with parameters
  var query = `
WITH daily_totals AS (
  SELECT
    Date,
    SUM(Value) AS daily_total
  FROM
    \`serene-lotus-403821.project1.projection1\`
  GROUP BY
    Date
  ORDER BY
    Date
)
SELECT
  Date,
  daily_total,
  SUM(daily_total) OVER (ORDER BY Date) + @initial_balance AS account_balance
FROM
  daily_totals;`;

  // Set the query parameters
  var queryConfig = {
    query: {
      parameterMode: 'NAMED',
      queryParameters: [
        {
          name: 'initial_balance',
          parameterType: {
            type: 'NUMERIC'
          },
          parameterValue: {
            value: 1000 // Change this to your initial balance
          }
        }
      ]
    }
  };

  // Authenticate with BigQuery
  var job = BigQuery.Jobs.query(query, projectId, queryConfig);
  var queryResults = BigQuery.Jobs.getQueryResults(job.jobReference.projectId, job.jobReference.jobId);

  // Get the results and write to the active Google Sheet
  var sheet = SpreadsheetApp.getActiveSheet();
  sheet.getRange(1, 1, queryResults.length, queryResults[0].length).setValues(queryResults);
}
