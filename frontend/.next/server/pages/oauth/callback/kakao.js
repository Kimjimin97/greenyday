"use strict";
/*
 * ATTENTION: An "eval-source-map" devtool has been used.
 * This devtool is neither made for production nor for readable output files.
 * It uses "eval()" calls to create a separate source file with attached SourceMaps in the browser devtools.
 * If you are trying to read the output file, select a different devtool (https://webpack.js.org/configuration/devtool/)
 * or disable the default devtool with "devtool: false".
 * If you are looking for production-ready output files, see mode: "production" (https://webpack.js.org/configuration/mode/).
 */
(() => {
var exports = {};
exports.id = "pages/oauth/callback/kakao";
exports.ids = ["pages/oauth/callback/kakao"];
exports.modules = {

/***/ "./src/pages/oauth/callback/kakao.js":
/*!*******************************************!*\
  !*** ./src/pages/oauth/callback/kakao.js ***!
  \*******************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   \"default\": () => (__WEBPACK_DEFAULT_EXPORT__)\n/* harmony export */ });\n/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react */ \"react\");\n/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_0__);\n\nconst Kakao = ()=>{\n    const [code, setcode] = (0,react__WEBPACK_IMPORTED_MODULE_0__.useState)(\"\");\n    // 인가코드\n    (0,react__WEBPACK_IMPORTED_MODULE_0__.useEffect)(()=>{\n        setcode(new URL(window.location.href).searchParams.get(\"code\"));\n    }, []);\n    console.log(code);\n};\n/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (Kakao);\n//# sourceURL=[module]\n//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiLi9zcmMvcGFnZXMvb2F1dGgvY2FsbGJhY2sva2FrYW8uanMuanMiLCJtYXBwaW5ncyI6Ijs7Ozs7O0FBQTRDO0FBRTVDLE1BQU1FLFFBQVEsSUFBTTtJQUNsQixNQUFNLENBQUNDLE1BQU1DLFFBQVEsR0FBR0gsK0NBQVFBLENBQUM7SUFDakMsT0FBTztJQUNQRCxnREFBU0EsQ0FBQyxJQUFNO1FBQ2RJLFFBQVEsSUFBSUMsSUFBSUMsT0FBT0MsUUFBUSxDQUFDQyxJQUFJLEVBQUVDLFlBQVksQ0FBQ0MsR0FBRyxDQUFDO0lBQ3pELEdBQUcsRUFBRTtJQUNMQyxRQUFRQyxHQUFHLENBQUNUO0FBQ2Q7QUFFQSxpRUFBZUQsS0FBS0EsRUFBQyIsInNvdXJjZXMiOlsid2VicGFjazovL2Zyb250ZW5kLy4vc3JjL3BhZ2VzL29hdXRoL2NhbGxiYWNrL2tha2FvLmpzPzliZGIiXSwic291cmNlc0NvbnRlbnQiOlsiaW1wb3J0IHsgdXNlRWZmZWN0LCB1c2VTdGF0ZSB9IGZyb20gXCJyZWFjdFwiO1xuXG5jb25zdCBLYWthbyA9ICgpID0+IHtcbiAgY29uc3QgW2NvZGUsIHNldGNvZGVdID0gdXNlU3RhdGUoXCJcIik7XG4gIC8vIOyduOqwgOy9lOuTnFxuICB1c2VFZmZlY3QoKCkgPT4ge1xuICAgIHNldGNvZGUobmV3IFVSTCh3aW5kb3cubG9jYXRpb24uaHJlZikuc2VhcmNoUGFyYW1zLmdldChcImNvZGVcIikpO1xuICB9LCBbXSk7XG4gIGNvbnNvbGUubG9nKGNvZGUpO1xufTtcblxuZXhwb3J0IGRlZmF1bHQgS2FrYW87XG4iXSwibmFtZXMiOlsidXNlRWZmZWN0IiwidXNlU3RhdGUiLCJLYWthbyIsImNvZGUiLCJzZXRjb2RlIiwiVVJMIiwid2luZG93IiwibG9jYXRpb24iLCJocmVmIiwic2VhcmNoUGFyYW1zIiwiZ2V0IiwiY29uc29sZSIsImxvZyJdLCJzb3VyY2VSb290IjoiIn0=\n//# sourceURL=webpack-internal:///./src/pages/oauth/callback/kakao.js\n");

/***/ }),

/***/ "react":
/*!************************!*\
  !*** external "react" ***!
  \************************/
/***/ ((module) => {

module.exports = require("react");

/***/ })

};
;

// load runtime
var __webpack_require__ = require("../../../webpack-runtime.js");
__webpack_require__.C(exports);
var __webpack_exec__ = (moduleId) => (__webpack_require__(__webpack_require__.s = moduleId))
var __webpack_exports__ = (__webpack_exec__("./src/pages/oauth/callback/kakao.js"));
module.exports = __webpack_exports__;

})();