/*
 * ATTENTION: The "eval" devtool has been used (maybe by default in mode: "development").
 * This devtool is neither made for production nor for readable output files.
 * It uses "eval()" calls to create a separate source file in the browser devtools.
 * If you are trying to read the output file, select a different devtool (https://webpack.js.org/configuration/devtool/)
 * or disable the default devtool with "devtool: false".
 * If you are looking for production-ready output files, see mode: "production" (https://webpack.js.org/configuration/mode/).
 */
/******/ (() => { // webpackBootstrap
/******/ 	var __webpack_modules__ = ({

/***/ "./js/app.js":
/*!*******************!*\
  !*** ./js/app.js ***!
  \*******************/
/***/ (() => {

eval("const dropdownArrow = document.querySelector(\".blog-list-dropdown-arrow\");\nconst dropdown = document.querySelector(\".blog-list-dropdown\");\n\ndocument.addEventListener(\"click\", (e) => {\n    if (e.target === dropdownArrow) {\n        if (dropdown.style.display === \"none\") {\n            dropdown.style.display = \"block\";\n        } else {\n            dropdown.style.display = \"none\";\n        }\n    } else if (e.target !== dropdown || e.target.parentElement !== dropdown) {\n        dropdown.style.display = \"none\";\n    }\n});\n\n\n//# sourceURL=webpack://assets/./js/app.js?");

/***/ })

/******/ 	});
/************************************************************************/
/******/ 	
/******/ 	// startup
/******/ 	// Load entry module and return exports
/******/ 	// This entry module can't be inlined because the eval devtool is used.
/******/ 	var __webpack_exports__ = {};
/******/ 	__webpack_modules__["./js/app.js"]();
/******/ 	
/******/ })()
;