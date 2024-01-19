function onOpen() {
  var ui = SpreadsheetApp.getUi();
  // Or DocumentApp or FormApp.
  ui.createMenu('Custom Menu')
      .addItem('Projection 1', 'month2day')
      .addSeparator()
      .addSubMenu(ui.createMenu('Sub-menu')
          .addItem('Projection 2', 'month2day2'))
          .addItem('Projection 3', 'month2day3')
      .addToUi();
}