const CreateSortableWidget = function(sortable_id) {
    var sortable_list_id = "#" + sortable_id + "_list";

    var refreshInputValue = function() {
        result = [];
        $(sortable_list_id).children(".sortable-widget-item").each(function(index, element) {
            result.push($(element).data("id"));
        });
        $("input#" + sortable_id).val(JSON.stringify(result));
    }

    sortable(sortable_list_id, {
        placeholder: '<div class="sortable-widget-placeholder">&nbsp;</div>'
    })[0].addEventListener("sortstop", function() {
        refreshInputValue();
    });

    refreshInputValue();
};
