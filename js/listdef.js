var options = {
  valueNames: [ 'title', 'format', 'category', 'description' ]
};

var contentList = new List('content-list', options);

$('#search-reset').click(function() {
  $('#search-field').val('');
  contentList.filter();
  contentList.search();
  return false;
});

$('#filter-wiki').click(function() {
  contentList.filter(function(item) {
    if (item.values().format == "Wiki") {
      return true;
    } else {
      return false;
    }
  });
  return false;
});

$('#filter-drive').click(function() {
  contentList.filter(function(item) {
    if (item.values().format == "Google Drive") {
      return true;
    } else {
      return false;
    }
  });
  return false;
});

$('#filter-blog').click(function() {
  contentList.filter(function(item) {
    if (item.values().format == "Blog") {
      return true;
    } else {
      return false;
    }
  });
  return false;
});

$('#filter-app').click(function() {
  contentList.filter(function(item) {
    if (item.values().format == "App") {
      return true;
    } else {
      return false;
    }
  });
  return false;
});

$('#filter-video').click(function() {
  contentList.filter(function(item) {
    if (item.values().format == "Video") {
      return true;
    } else {
      return false;
    }
  });
  return false;
});

$('#filter-photo').click(function() {
  contentList.filter(function(item) {
    if (item.values().format == "Photo") {
      return true;
    } else {
      return false;
    }
  });
  return false;
});

$('#filter-literature').click(function() {
  contentList.filter(function(item) {
    if (item.values().format == "Literature") {
      return true;
    } else {
      return false;
    }
  });
  return false;
});

$('#filter-review').click(function() {
  contentList.filter(function(item) {
    if (item.values().format == "Review") {
      return true;
    } else {
      return false;
    }
  });
  return false;
});


$('#filter-finance').click(function() {
  contentList.filter(function(item) {
    if (item.values().category == "Finance") {
      return true;
    } else {
      return false;
    }
  });
  return false;
});

$('#filter-education').click(function() {
  contentList.filter(function(item) {
    if (item.values().category == "Education") {
      return true;
    } else {
      return false;
    }
  });
  return false;
});


$('#filter-technology').click(function() {
  contentList.filter(function(item) {
    if (item.values().category == "Technology") {
      return true;
    } else {
      return false;
    }
  });
  return false;
});

$('#filter-science').click(function() {
  contentList.filter(function(item) {
    if (item.values().category == "Science") {
      return true;
    } else {
      return false;
    }
  });
  return false;
});

$('#filter-fun').click(function() {
  contentList.filter(function(item) {
    if (item.values().category == "Fun") {
      return true;
    } else {
      return false;
    }
  });
  return false;
});
