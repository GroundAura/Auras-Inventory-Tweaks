BarterMenu.as

	// @override ItemMenu
	public function setConfig(a_config: Object): Void
	{
		super.setConfig(a_config);

		var itemList: TabularList = inventoryLists.itemList;		
		itemList.addDataProcessor(new BarterDataSetter(_buyMult, _sellMult));
		itemList.addDataProcessor(new InventoryIconSetter(a_config["Appearance"]));
		itemList.addDataProcessor(new PropertyDataExtender(a_config["Appearance"], a_config["Properties"], "itemProperties", "itemIcons", "itemCompoundProperties"));
		
		var layout: ListLayout = ListLayoutManager.createLayout(a_config["ListLayout"], "ItemListLayout");
		itemList.layout = layout;

		// Not 100% happy with doing this here, but has to do for now.
		if (inventoryLists.categoryList.selectedEntry)
			layout.changeFilterFlag(inventoryLists.categoryList.selectedEntry.flag);
	}






ContainerMenu.as

	// @override ItemMenu
	public function setConfig(a_config: Object): Void
	{
		super.setConfig(a_config);
		
		var itemList: TabularList = inventoryLists.itemList;		
		itemList.addDataProcessor(new InventoryDataSetter());
		itemList.addDataProcessor(new InventoryIconSetter(a_config["Appearance"]));
		itemList.addDataProcessor(new PropertyDataExtender(a_config["Appearance"], a_config["Properties"], "itemProperties", "itemIcons", "itemCompoundProperties"));
		
		var layout: ListLayout = ListLayoutManager.createLayout(a_config["ListLayout"], "ItemListLayout");
		itemList.layout = layout;

		// Not 100% happy with doing this here, but has to do for now.
		if (inventoryLists.categoryList.selectedEntry)
			layout.changeFilterFlag(inventoryLists.categoryList.selectedEntry.flag);
			
		_equipModeKey = a_config["Input"].controls.pc.equipMode;
		_equipModeControls = {keyCode: _equipModeKey};
	}






GiftMenu.as

	// @override ItemMenu
	public function setConfig(a_config: Object): Void
	{
		super.setConfig(a_config);

		var itemList: TabularList = inventoryLists.itemList;		
		itemList.addDataProcessor(new InventoryDataSetter());
		itemList.addDataProcessor(new InventoryIconSetter(a_config["Appearance"]));
		itemList.addDataProcessor(new PropertyDataExtender(a_config["Appearance"], a_config["Properties"], "itemProperties", "itemIcons", "itemCompoundProperties"));
		
		var layout: ListLayout = ListLayoutManager.createLayout(a_config["ListLayout"], "ItemListLayout");
		itemList.layout = layout;

		// Not 100% happy with doing this here, but has to do for now.
		if (inventoryLists.categoryList.selectedEntry)
			layout.changeFilterFlag(inventoryLists.categoryList.selectedEntry.flag);
	}






InventoryMenu.as

	// @override ItemMenu
	public function setConfig(a_config: Object): Void
	{
		super.setConfig(a_config);
		
		var itemList: TabularList = inventoryLists.itemList;
		itemList.addDataProcessor(new InventoryDataSetter());
		itemList.addDataProcessor(new InventoryIconSetter(a_config["Appearance"]));
		itemList.addDataProcessor(new PropertyDataExtender(a_config["Appearance"], a_config["Properties"], "itemProperties", "itemIcons", "itemCompoundProperties"));
		
		var layout: ListLayout = ListLayoutManager.createLayout(a_config["ListLayout"], "ItemListLayout");
		itemList.layout = layout;

		// Not 100% happy with doing this here, but has to do for now.
		if (inventoryLists.categoryList.selectedEntry)
			layout.changeFilterFlag(inventoryLists.categoryList.selectedEntry.flag);
	}






MagicMenu.as

	// @override ItemMenu
	public function setConfig(a_config: Object): Void
	{
		super.setConfig(a_config);
		
		var itemList: TabularList = inventoryLists.itemList;
		itemList.addDataProcessor(new MagicDataSetter(a_config["Appearance"]));
		itemList.addDataProcessor(new MagicIconSetter(a_config["Appearance"]));
		itemList.addDataProcessor(new PropertyDataExtender(a_config["Appearance"], a_config["Properties"], "magicProperties", "magicIcons", "magicCompoundProperties"));
		
		var layout: ListLayout = ListLayoutManager.createLayout(a_config["ListLayout"], "MagicListLayout");
		itemList.layout = layout;

		// Not 100% happy with doing this here, but has to do for now.
		if (inventoryLists.categoryList.selectedEntry)
			layout.changeFilterFlag(inventoryLists.categoryList.selectedEntry.flag);
	}






CraftingMenu.as

	private function onConfigLoad(event: Object): Void
	{
		setConfig(event.config);
		
		CategoryList.showPanel();
	}
	
	private function setConfig(a_config: Object): Void
	{
		_config = a_config;
		ItemList.addDataProcessor(new CraftingDataSetter());
		ItemList.addDataProcessor(new CraftingIconSetter(a_config["Appearance"]));

		positionFloatingElements();
		
		var itemListState = CategoryList.itemList.listState;
		var appearance = a_config["Appearance"];
		
		itemListState.iconSource = appearance.icons.item.source;
		itemListState.showStolenIcon = appearance.icons.item.showStolen;
		
		itemListState.defaultEnabledColor = appearance.colors.text.enabled;
		itemListState.negativeEnabledColor = appearance.colors.negative.enabled;
		itemListState.stolenEnabledColor = appearance.colors.stolen.enabled;
		itemListState.defaultDisabledColor = appearance.colors.text.disabled;
		itemListState.negativeDisabledColor = appearance.colors.negative.disabled;
		itemListState.stolenDisabledColor = appearance.colors.stolen.disabled;
		
		var layout: ListLayout;
		
		if (_subtypeName == "EnchantConstruct") {
			layout = ListLayoutManager.createLayout(a_config["ListLayout"], "EnchantListLayout");
			
		} else if (_subtypeName == "Smithing") {
			layout = ListLayoutManager.createLayout(a_config["ListLayout"], "SmithingListLayout");
			
		} else if (_subtypeName == "ConstructibleObject") {			
			layout = ListLayoutManager.createLayout(a_config["ListLayout"], "ConstructListLayout");
			
		} else /*if (_subtypeName == "Alchemy")*/ {
			layout = ListLayoutManager.createLayout(a_config["ListLayout"], "AlchemyListLayout");
			layout.entryWidth -= CraftingLists.SHORT_LIST_OFFSET;
		}
		
		ItemList.layout = layout;
		
		var previousColumnKey = a_config["Input"].controls.gamepad.prevColumn;
		var nextColumnKey = a_config["Input"].controls.gamepad.nextColumn;
		var sortOrderKey = a_config["Input"].controls.gamepad.sortOrder;
		_sortColumnControls = [{keyCode: previousColumnKey},
							   {keyCode: nextColumnKey}];
		_sortOrderControls = {keyCode: sortOrderKey};
		
		_searchKey = a_config["Input"].controls.pc.search;
		_searchControls = {keyCode: _searchKey};
	}


















ConfigManager.as

import flash.utils.*;
import gfx.events.EventDispatcher;

import skyui.components.list.ListLayout;
import skyui.util.GlobalFunctions;


class skyui.util.ConfigManager
{
  /* CONSTANTS */
  
	private static var CONFIG_PATH = "skyui/config.txt";
	private static var TIMEOUT = 3000;
	
	private static var LOAD_NONE = 0;
	private static var LOAD_FILE = 1;
	private static var LOAD_PAPYRUS = 2;
	
	
  /* PRIVATE VARIABLES */
  
	private static var _constantTable: Object = {
		
		ASCENDING: 0,
		DESCENDING: Array.DESCENDING,
		CASEINSENSITIVE: Array.CASEINSENSITIVE,
		NUMERIC: Array.NUMERIC
	};
	
	// Contains names of classes
	private static var _extConstantTableNames: Array = [];
	// Contains the actual classes.
	private static var _extConstantTables: Object = {};
	
	private static var _eventDummy: Object;
	
	// 0: Waiting for file, 1: Waiting for override 2: Loaded
	private static var _loadPhase: Number = LOAD_NONE;
	
	private static var _config: Object;
	
	private static var _timeoutID: Number;
	
	
  /* INITIALIATZION */
  
  	private static var _initialized:Boolean = initialize();
  
	private static function initialize(): Boolean
	{
		GlobalFunctions.addArrayFunctions();
		
		_eventDummy = {};
		EventDispatcher.initialize(_eventDummy);
		
		var lv = new LoadVars();
		lv.onData = parseData;
		lv.load(CONFIG_PATH);
		
		return true;
	}
	
	
  /* PAPYRUS INTERFACE */
  
  	// Key/value pairs "Section$k$e$y$" / "value"
	public static var out_overrides = {};
	public static var in_overrideKeys = [];
	
	public static function setExternalOverrideKeys()
	{
		in_overrideKeys.splice(0);
		
		for (var i = 0; i < arguments.length; i++)
			in_overrideKeys[i] = arguments[i];
	}
	
	public static function setExternalOverrideValues()
	{
		// Received overrides before file? This can't be right.
		if (_loadPhase == LOAD_NONE)
			return;
		
		// Update happens in 2 phases.
		// First the keys are sent and stored, then the values are sent and immediately processed.
		for (var i = 0; i < arguments.length; i++) {
			var t = in_overrideKeys[i];
			if (t && t != "")
				parseExternalOverride(t, arguments[i]);
		}
		
		if (_loadPhase != LOAD_PAPYRUS) {
			clearInterval(_timeoutID);
			delete _timeoutID;
			
			_loadPhase = LOAD_PAPYRUS;
			_eventDummy.dispatchEvent({type: "configLoad", config: _config});			
		} else {
			// Timeout
			_eventDummy.dispatchEvent({type: "configUpdate", config: _config});
		}
	}
	
	
  /* PUBLIC FUNCTIONS */
  
	public static function registerLoadCallback(a_scope: Object, a_callBack: String): Void
	{
		_eventDummy.addEventListener("configLoad", a_scope, a_callBack);
	}
	
	public static function registerUpdateCallback(a_scope: Object, a_callBack: String): Void
	{
		_eventDummy.addEventListener("configUpdate", a_scope, a_callBack);
	}
	
	public static function setConstant(a_name: String, a_value): Void
	{
		var type = typeof(a_value);
		if (type != "number" && type != "boolean" && type != "string")
			return;
		
		_constantTable[a_name] = a_value;
	}
	
	
	public static function addConstantTable(a_name: String, a_class: Function): Void
	{
		_extConstantTableNames.push(a_name);
	}
	
	public static function getConstant(a_name: String)
	{
		if (_constantTable[a_name] != undefined)
			return _constantTable[a_name];
		
		var a: Array = a_name.split(".");

		if (a.length < 2)
			return undefined;

		var className: String = a[a.length - 2];
		var constName: String = a[a.length - 1];

		if (_extConstantTables[className][constName] != undefined)
			return _extConstantTables[className][constName];

		return undefined;
	}
	
	public static function setOverride(a_section: String, a_key: String, a_value, a_valueStr: String): Void
	{
		// Allow to add new sections
		if (_config[a_section] == undefined)
			_config[a_section] = {};
		
		var a = a_key.split(".");

		// Prepare key subsections
		var loc = _config[a_section];

		var varContainer = null;
		if (a[0] == "vars")
			varContainer = loc.vars[a[1]];
		
		for (var j=0; j<a.length-1; j++) {
			if (loc[a[j]] == undefined)
				loc[a[j]] = {};
			loc = loc[a[j]];
		}

		// Store value in config
		loc[a[a.length-1]] = a_value;
		
		// UI functions would try to look up keys.a.b.c, instead of keys["a.b.c"].
		// . -> $
		a_key = a_key.split(".").join("$");
		
		var ovrKey = a_section + "$" + a_key;
		out_overrides[ovrKey] = a_valueStr;
		skse.SendModEvent("SKICO_setConfigOverride", ovrKey);
		
		// If we changed the value of a var, update all recorded references.
		if (varContainer) {
			for (var i=0; i<varContainer._refLocs.length; i++) {
				var varLoc = varContainer._refLocs[i];
				var varKey = varContainer._refKeys[i];
				varLoc[varKey] = a_value;
			}
		}
		
		_eventDummy.dispatchEvent({type: "configUpdate", config: _config});
	}
	
	// (Unsafe) Provide static accessor to the config to retrieve trivial values
	/*
	public static function getValue(a_section: String, a_key: String): Object
	{
		if (_loadPhase < LOAD_PAPYRUS)
			return null;
		
		var a = a_key.split(".");
		var loc = _config[a_section];
		for (var j=0; j<a.length; j++) {
			if (loc[a[j]] == undefined)
				return null;
			loc = loc[a[j]];
		}
		
		return loc;
	}*/


  /* PRIVATE FUNCTIONS */
  
	
	private static function parseExternalOverride(a_key: String, a_valueStr: String): Void
	{
		var index =  a_key.indexOf("$");
		
		// raw key: section$k$e$y
		var section = GlobalFunctions.clean(a_key.slice(0, index));
		var key = GlobalFunctions.clean(a_key.slice(index + 1));
		var val = parseValueString(GlobalFunctions.clean(a_valueStr), null);

		// Prepare key subsections - external keys use $ as separator
		var a = key.split("$");
		var loc = _config[section];
		
		var varContainer = null;
		if (a[0] == "vars")
			varContainer = loc.vars[a[1]];
		
		for (var j=0; j<a.length-1; j++) {
			if (loc[a[j]] == undefined)
				loc[a[j]] = {};
			loc = loc[a[j]];
		}
		
		loc[a[a.length-1]] = val;
		
		// If we changed the value of a var, update all recorded references.
		if (varContainer) {
			for (var i=0; i<varContainer._refLocs.length; i++) {
				var varLoc = varContainer._refLocs[i];
				var varKey = varContainer._refKeys[i];
				varLoc[varKey] = val;
			}
		}
	}

	private static function parseData(a_data:Array): Void
	{
		_config = {};
		
		// Resolve constant tables
		for (var i=0; i<_extConstantTableNames.length; i++) {
			var a = _extConstantTableNames[i].split(".");
			var className: String = a[a.length - 1];
			var tbl = _global[a[0]];
			for (var j=1; j<a.length; j++)
				tbl = tbl[a[j]];
			_extConstantTables[className] = tbl;
		}
		
		var lines = a_data.split("\r\n");
		if (lines.length == 1)
			lines = a_data.split("\n");

		var section = undefined;

		for (var i = 0; i < lines.length; i++) {

			// Comment
			if (lines[i].charAt(0) == ";")
				continue;

			// Section start
			if (lines[i].charAt(0) == "[") {
				section = lines[i].slice(1, lines[i].lastIndexOf("]"));
				
				if (_config[section] == undefined)
					_config[section] = {};
					
				continue;
			}

			if (lines[i].length < 3 || section == undefined)
				continue;
			
			// Get raw key string
			var key = GlobalFunctions.clean(lines[i].slice(0, lines[i].indexOf("=")));
			if (key == undefined)
				continue;
				
			// Prepare key subsections
			var a = key.split(".");
			var loc = _config[section];
			for (var j=0; j<a.length-1; j++) {
				if (loc[a[j]] == undefined)
					loc[a[j]] = {};
				loc = loc[a[j]];
			}

			// Detect value type & extract
			var val = parseValueString(GlobalFunctions.clean(lines[i].slice(lines[i].indexOf("=") + 1)), _config[section], loc, a[a.length-1]);
			
			if (val == undefined)
				continue;

			// Store val at config.section.a.b.c.d
			loc[a[a.length-1]] = val;
		}
		
		_loadPhase = LOAD_FILE;
		_timeoutID = setInterval(onTimeout, TIMEOUT);
		
//		_eventDummy.dispatchEvent({type: "configLoad", config: _config});
	}
	
	private static function onTimeout(): Void
	{
		clearInterval(_timeoutID);
		delete _timeoutID;

		if (_loadPhase != LOAD_PAPYRUS) {
			_loadPhase = LOAD_PAPYRUS;
			_eventDummy.dispatchEvent({type: "configLoad", config: _config});
		}
	}
	
	private static function parseValueString(a_str: String, a_root: Object, a_loc: Object, a_key: String): Object
	{
		if (a_str == undefined)
			return undefined;
			
		var t = undefined;

		// Number?
		if (!isNaN(a_str)) {
			return Number(a_str);
			
		// Bool true?
		} else if (a_str.toLowerCase() == "true") {
			return true;
			
		// Bool false?
		} else if (a_str.toLowerCase() == "false") {
			return false;

		// Undefined?
		} else if (a_str.toLowerCase() == "undefined") {
			return undefined;
			
		// Explicit String?
		} else if (a_str.charAt(0) == "'") {
			return GlobalFunctions.extract(a_str, "'", "'");
			
		// Entry property? - substituted later
		} else if (a_str.charAt(0) == "@") {
			return a_str;

		// Associative array?
		//TODO: This should properly check if [:,] is within a string
		//      As should the List parsing below
		} else if (a_str.charAt(0) == "<" && a_str.indexOf(":") != -1) {
			var assocArray = new Object();
			var pairs =  GlobalFunctions.extract(a_str, "<", ">").split(",");
			for (var i=0; i<pairs.length; i++) {
				var keyValue = pairs[i].split(":");
				if (keyValue.length != 2) {
					// If we don't have a pair we just ignore it
					continue;
				}
				var key = parseValueString(GlobalFunctions.clean(keyValue[0]), a_root, null, null);
				var val = parseValueString(GlobalFunctions.clean(keyValue[1]), a_root, assocArray, key);
				assocArray[key] = val;
			}
			return assocArray;

		// List?
		} else if (a_str.charAt(0) == "<") {
			if (a_str.charAt(1) == ">")
				return new Array();
			var values = GlobalFunctions.extract(a_str, "<", ">").split(",");
			for (var i=0; i<values.length; i++)
				values[i] = parseValueString(GlobalFunctions.clean(values[i]), a_root, values, i);
				
			return values;
			
		// Flags?
		} else if (a_str.charAt(0) == "{") {
			var values = GlobalFunctions.extract(a_str, "{", "}").split("|");
			var flags = 0;
			for (var i=0; i<values.length; i++) {
				t = parseValueString(GlobalFunctions.clean(values[i]), a_root, a_loc, a_key);
				if (isNaN(t))
					return undefined;
					
				flags = flags | t;
			}
			return flags;
		
		// Constant?
		} else if ((t = getConstant(a_str)) != undefined) {
			return t;
			
		// Var?
		} else if (a_root.vars[a_str] != undefined) {
			// A variable might be updated later via overrides, in which case we'd have to re-evaluate previous
			// expressions that used it. To make that efficient, each variable stores it's references.
			// Because we can't store pointers, this has to be the object/key pair (aka loc/name).
			if (a_loc && a_key) {
				if (a_root.vars[a_str]._refLocs == undefined) {
					a_root.vars[a_str]._refLocs = [];
					a_root.vars[a_str]._refKeys = [];
				}
				
				// Can be either object+string or array+index
				a_root.vars[a_str]._refLocs.push(a_loc);
				a_root.vars[a_str]._refKeys.push(a_key);
			}
			
			return a_root.vars[a_str].value;
		}
		
		// Default String
		return a_str;
	}
}
























SKI_SettingsManager.psc

scriptname SKI_SettingsManager extends SKI_QuestBase  

; CONSTANTS ---------------------------------------------------------------------------------------

string property		MENU_ROOT		= "_global.skyui.util.ConfigManager" autoReadonly

string property		INVENTORY_MENU	= "InventoryMenu" autoReadonly
string property		MAGIC_MENU		= "MagicMenu" autoReadonly
string property		CONTAINER_MENU	= "ContainerMenu" autoReadonly
string property		BARTER_MENU		= "BarterMenu" autoReadonly
string property		GIFT_MENU		= "GiftMenu" autoReadonly
string property		CRAFTING_MENU	= "Crafting Menu" autoReadonly


; PRIVATE VARIABLES -------------------------------------------------------------------------------

int			_overrideCount	= 0
string[]	_overrideKeys
string[]	_overrideValues

string		_currentMenu


; INITIALIZATION ----------------------------------------------------------------------------------

event OnInit()
	_overrideKeys	= new string[128]
	_overrideValues	= new string[128]

	int i = 0
	while (i<128)
		_overrideKeys[i] = ""
		_overrideValues[i] = ""
		i += 1
	endWhile

	OnGameReload()
endEvent

; @implements SKI_QuestBase
event OnGameReload()
	RegisterForMenu(INVENTORY_MENU)
	RegisterForMenu(MAGIC_MENU)
	RegisterForMenu(CONTAINER_MENU)
	RegisterForMenu(BARTER_MENU)
	RegisterForMenu(GIFT_MENU)
	RegisterForMenu(CRAFTING_MENU)
	RegisterForModEvent("SKICO_setConfigOverride", "OnSetConfigOverride")
endEvent


; EVENTS ------------------------------------------------------------------------------------------

event OnMenuOpen(string a_menuName)
	GotoState("LOCKED")
	; Check if its still open
	if (UI.IsMenuOpen(a_menuName))
		_currentMenu = a_menuName
		UI.InvokeStringA(a_menuName, MENU_ROOT + ".setExternalOverrideKeys", _overrideKeys)
		UI.InvokeStringA(a_menuName, MENU_ROOT + ".setExternalOverrideValues", _overrideValues)
	endIf
	GotoState("")
endEvent

event OnSetConfigOverride(string a_eventName, string a_strArg, float a_numArg, Form a_sender)
	string overrideKey = a_strArg
	string overrideValue = UI.GetString(_currentMenu, MENU_ROOT + ".out_overrides." + overrideKey)

	SetOverride(overrideKey, overrideValue)
endEvent

; ----------------------------------------------
state LOCKED

event OnMenuOpen(string a_menuName)
endEvent

endState


; FUNCTIONS ---------------------------------------------------------------------------------------

; @interface
bool function SetOverride(string a_key, string a_value)
	if (a_key == "")
		return false
	endIf

	; Existing override?
	int index = _overrideKeys.Find(a_key)
	if (index != -1)
		_overrideValues[index] = a_value

		return true

	; New override
	else
		if (_overrideCount >= 128)
			return false
		endIf

		index = NextFreeIndex()
		if (index == -1)
			return false
		endIf

		_overrideKeys[index] = a_key
		_overrideValues[index] = a_value
		_overrideCount += 1

		return true
	endIf

endFunction

; @interface
bool function ClearOverride(string a_key)
	if (a_key == "")
		return false
	endIf

	int index = _overrideKeys.Find(a_key)
	if (index == -1)
		return false
	endIf
	
	_overrideKeys[index] = ""
	_overrideValues[index] = ""
	_overrideCount -= 1
	
	return true
endFunction

int function NextFreeIndex()
	int i = 0
	
	while (i < _overrideKeys.length)
		if (_overrideKeys[i] == "")
			return i
		endIf
		i += 1
	endWhile

	return -1
endFunction


