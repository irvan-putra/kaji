// Shared Tangle widgets for the Kaji cook collection.
Tangle.classes.TKFlag = {
    initialize: function (element, options, tangle, variable) {
        element.addEvent("click", function () {
            tangle.setValue(variable, tangle.getValue(variable) ? 0 : 1);
        });
    },
    update: function (element, value) {
        element.textContent = value ? "on" : "off";
    }
};

Tangle.classes.TKSingularPlural = {
    update: function (element, value) {
        var showIndex = (value === 1) ? 0 : 1;
        element.getChildren().each(function (child, index) {
            if (index === showIndex) { child.style.removeProperty("display"); }
            else { child.style.display = "none"; }
        });
    }
};

Tangle.classes.TKDynamicRowspan = {
    update: function (element, value) {
        element.rowSpan = Math.max(1, Math.round(value));
    }
};

function joinList(items) {
    return items.length === 1 ? items[0] :
        items.slice(0, -1).join(", ") + " and " + items[items.length - 1];
}
