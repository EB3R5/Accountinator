function sumRowsBySpendConfiguration() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var provisionSheet = ss.getSheetByName("Provision");
  var data = provisionSheet.getDataRange().getValues();
  
  // Define the column index for the "Spend Configuration" column
  var spendConfigColumnIndex = 2; // 0-based index
  var amountColumnIndex = 12; // 0-based index

  // Create an object to store the sums by Spend Configuration
  var spendConfigSums = {};

  // Iterate through the data
  for (var i = 1; i < data.length; i++) { // Skip the header row (assumes the first row is a header)
    var spendConfig = data[i][spendConfigColumnIndex];
    var amount = data[i][amountColumnIndex]; // Assuming "Amount" is in the 13th column (0-based index)

    // If the Spend Configuration exists in the object, add to the sum
    if (spendConfig in spendConfigSums) {
      spendConfigSums[spendConfig] += amount;
    } else {
      // Otherwise, initialize the sum for the Spend Configuration
      spendConfigSums[spendConfig] = amount;
    }
  }

  // Log the Spend Configuration sums
  for (var key in spendConfigSums) {
    Logger.log("Spend Configuration: " + key + ", Total Amount: " + spendConfigSums[key]);
  }
}
