function reshapeAndAddToProjection() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var provisionSheet = ss.getSheetByName("Provision");
  var projectionSheet = ss.getSheetByName("Add Projection");
  var data = provisionSheet.getDataRange().getValues();
  
  // Define the column indices on the "Provision" sheet
  var spendConfigColumnIndex = 2; // 0-based index
  var amountColumnIndex = 12; // 0-based index
  var dateColumnIndex = 3; // 0-based index

  // Create an object to store the sums by Spend Configuration and month
  var spendConfigMonthSums = {};

  // Iterate through the data on the "Provision" sheet
  for (var i = 1; i < data.length; i++) { // Skip the header row (assumes the first row is a header)
    var spendConfig = data[i][spendConfigColumnIndex];
    var amount = data[i][amountColumnIndex]; // Assuming "Amount" is in the 13th column (0-based index)
    var date = new Date(data[i][dateColumnIndex]); // Convert the date to a JavaScript Date object

    var year = date.getFullYear();
    var month = date.getMonth();

    // Create a unique key for each Spend Configuration and month
    var key = spendConfig + "_" + year + "_" + month;

    // If the key exists in the object, add to the sum
    if (key in spendConfigMonthSums) {
      spendConfigMonthSums[key] += amount;
    } else {
      // Otherwise, initialize the sum for the key
      spendConfigMonthSums[key] = amount;
    }
  }

  // Create rows in "Add Projection" based on the sums
  for (var key in spendConfigMonthSums) {
    var parts = key.split("_");
    var spendConfig = parts[0];
    var year = parseInt(parts[1]);
    var month = parseInt(parts[2]) + 1; // Add 1 to convert from 0-based to 1-based month
    var amount = spendConfigMonthSums[key];

    // Append the reshaped row to the "Add Projection" sheet
    projectionSheet.appendRow([spendConfig, "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", year, month, amount]);
  }
}
