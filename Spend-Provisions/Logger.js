function sumRowsByCategory() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var provisionSheet = ss.getSheetByName("Provision");
  var data = provisionSheet.getDataRange().getValues();
  
  // Define the column index for the "Category" column
  var categoryColumnIndex = 5; // 0-based index

  // Create an object to store the sums by category
  var categorySums = {};

  // Iterate through the data
  for (var i = 1; i < data.length; i++) { // Skip the header row (assumes the first row is a header)
    var category = data[i][categoryColumnIndex];
    var amount = data[i][12]; // Assuming "Amount" is in the 13th column (0-based index)

    // If the category exists in the object, add to the sum
    if (category in categorySums) {
      categorySums[category] += amount;
    } else {
      // Otherwise, initialize the sum for the category
      categorySums[category] = amount;
    }
  }

  // Log the category sums
  for (var key in categorySums) {
    Logger.log("Category: " + key + ", Total Amount: " + categorySums[key]);
  }
}
