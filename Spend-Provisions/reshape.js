function copyDataToProjection() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var provisionSheet = ss.getSheetByName("Provision");
  var projectionSheet = ss.getSheetByName("Add Projection");
  
  // Define the columns to match on "Provision" sheet
  var spendTypeColumn = 1; // 0-based index
  var dateColumn = 3; // 0-based index

  // Define the columns on "Add Projection" sheet
  var categoryColumn = 0;
  var groupColumn = 1;
  var typeColumn = 2;
  var cashflowTypeColumn = 3;
  var budgetColumn = 4;

  var projectionData = projectionSheet.getDataRange().getValues();

  for (var i = 1; i < projectionData.length; i++) { // Skip the header row
    var category = projectionData[i][categoryColumn];
    var group = projectionData[i][groupColumn];
    var type = projectionData[i][typeColumn];
    var cashflowType = projectionData[i][cashflowTypeColumn];
    var budget = projectionData[i][budgetColumn];
    

    var sum = 0;

    // Loop through "Provision" sheet to find matching rows
    for (var j = 1; j < provisionData.length; j++) { // Skip the header row
      var spendType = provisionData[j][spendTypeColumn];
      var date = provisionData[j][dateColumn];

      // Check if the row in "Provision" matches the criteria
      if (spendType === type && date === "desired_date") {
        // Sum the "Amount" column
        sum += provisionData[j][12]; // Assuming "Amount" is in the 12th column (0-based index)
      }
    }

    // Set the corresponding month's value
    projectionData[i][5] = sum; // Assuming "Jan" is in the 5th column (0-based index)
    // You can repeat this for other months as needed

    // Append the updated row to the "Add Projection" sheet
    projectionSheet.getRange(i + 1, 1, 1, projectionData[0].length).setValues([projectionData[i]]);
  }
}
 sourceData[22],
    "Aug": sourceData[23],
    "Sept": sourceData[24],
    "Oct": sourceData[25],
    "Nov": sourceData[26],
    "Dec": sourceData[27],
    "Year Total": "",
  };

  // Combine the mapped columns and target columns into a single row
  var reshapedRow = { ...columnMapping, ...targetRow };

  // Convert the reshaped row into an array
  var reshapedRowArray = Object.values(reshapedRow);

  return reshapedRowArray;
}

// Example usage:
var sourceRow = [
  "Priority",
  "Spend Type",
  "Spend Configuration",
  "Date",
  "Description",
  "Category",
  "Group",
  "Type",
  "Cashflow Type",
  "Budget",
  // ... (other source columns)
];

var reshapedRowArray = reshapeData(sourceRow);
console.log(reshapedRowArray);

