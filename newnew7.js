function organizeAndAddRowsToProjectionByCategory() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var provisionSheet = ss.getSheetByName("Provision");
  var projectionSheet = ss.getSheetByName("Add Projection");
  var data = provisionSheet.getDataRange().getValues();

  // Define the column indices for the "Provision" sheet
  var spendConfigColumnIndex = 2; // 0-based index
  var categoryColumnIndex = 5; // 0-based index
  var groupColumnIndex = 6; // 0-based index
  var typeColumnIndex = 7; // 0-based index
  var cashflowTypeColumnIndex = 8; // 0-based index
  var budgetColumnIndex = 9; // 0-based index
  var amountColumnIndex = 12; // 0-based index
  var dateColumnIndex = 3; // 0-based index

  // Create an object to store the organized data
  var organizedData = {};

  // Define a function to format the amount as currency
  function formatAmountAsCurrency(amount) {
    return "$" + amount.toFixed(2); // Assuming USD, adjust the currency symbol as needed
  }

  // Iterate through the data
  for (var i = 1; i < data.length; i++) { // Skip the header row (assumes the first row is a header)
    var spendConfig = data[i][spendConfigColumnIndex];
    var category = data[i][categoryColumnIndex];
    var group = data[i][groupColumnIndex];
    var type = data[i][typeColumnIndex];
    var cashflowType = data[i][cashflowTypeColumnIndex];
    var budget = data[i][budgetColumnIndex];
    var amount = parseFloat(data[i][amountColumnIndex]); // Convert the amount to a number
    var date = new Date(data[i][dateColumnIndex]);

    // Check if there is a valid date
    if (isNaN(date.getTime())) {
      // Skip rows without a date
      continue;
    }

    var year = date.getFullYear();
    var month = date.getMonth();

    // Determine the target month row based on the date
    var targetRow = (year === new Date().getFullYear() && month === new Date().getMonth()) ? 18 + month : (month + 8); // 8 is used to offset rows to start from row 9

    // Create a unique key for each combination
    var key = category + "_" + group + "_" + type + "_" + cashflowType + "_" + budget;

    // If the key exists in the object, add to the amount for the appropriate month
    if (key in organizedData) {
      organizedData[key][targetRow] = formatAmountAsCurrency(parseFloat(organizedData[key][targetRow]) + amount);
      organizedData[key][30] = formatAmountAsCurrency(parseFloat(organizedData[key][30]) + amount); // Add to the "Year Total" column (row U)
    } else {
      // Otherwise, initialize the object for the key
      organizedData[key] = [category, group, type, cashflowType, budget];
      for (var j = 0; j < 12; j++) {
        organizedData[key].push(j === (targetRow - 9) ? formatAmountAsCurrency(amount) : '');
      }
      organizedData[key].push('', '', '', '', '', '', '', '', '', '', '', '', formatAmountAsCurrency(amount)); // Initialize the "Year Total" column (row U)
    }
  }

  // Add rows to the "Add Projection" sheet
  for (var key in organizedData) {
    var rowData = organizedData[key];
    projectionSheet.appendRow(rowData);
  }
}
