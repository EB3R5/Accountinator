function reshapeAndSumBySpendType() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var provisionSheet = ss.getSheetByName("Provision");
  var projectionSheet = ss.getSheetByName("Add Projection");
  
  // Define the columns on "Provision" sheet
  var spendTypeColumn = 1; // 0-based index
  var amountColumn = 12; // 0-based index

  // Define the columns on "Add Projection" sheet
  var categoryColumn = 0;
  var groupColumn = 1;
  var typeColumn = 2;
  var cashflowTypeColumn = 3;
  var budgetColumn = 4;

  var projectionData = projectionSheet.getDataRange().getValues();

  for (var i = 1; i < projectionData.length; i++) { // Skip the header row
    var type = projectionData[i][typeColumn]; // Assuming "Type" is in the 3rd column (0-based index)
    
    var sum = 0;

    // Loop through "Provision" sheet to find matching rows based on Spend Type
    for (var j = 1; j < provisionData.length; j++) { // Skip the header row
      var spendType = provisionData[j][spendTypeColumn];

      if (spendType === type) {
        // Sum the "Amount" column for the matching Spend Type
        sum += provisionData[j][amountColumn];
      }
    }

    // Set the summed value in the corresponding month's column
    projectionData[i][5] = sum; // Assuming "Jan" is in the 6th column (0-based index)
    // You can repeat this for other months as needed

    // Append the updated row to the "Add Projection" sheet
    projectionSheet.getRange(i + 1, 1, 1, projectionData[0].length).setValues([projectionData[i]]);
  }
}
