/******/ (function(modules) { // webpackBootstrap
/******/ 	// The module cache
/******/ 	var installedModules = {};
/******/
/******/ 	// The require function
/******/ 	function __webpack_require__(moduleId) {
/******/
/******/ 		// Check if module is in cache
/******/ 		if(installedModules[moduleId]) {
/******/ 			return installedModules[moduleId].exports;
/******/ 		}
/******/ 		// Create a new module (and put it into the cache)
/******/ 		var module = installedModules[moduleId] = {
/******/ 			i: moduleId,
/******/ 			l: false,
/******/ 			exports: {}
/******/ 		};
/******/
/******/ 		// Execute the module function
/******/ 		modules[moduleId].call(module.exports, module, module.exports, __webpack_require__);
/******/
/******/ 		// Flag the module as loaded
/******/ 		module.l = true;
/******/
/******/ 		// Return the exports of the module
/******/ 		return module.exports;
/******/ 	}
/******/
/******/
/******/ 	// expose the modules object (__webpack_modules__)
/******/ 	__webpack_require__.m = modules;
/******/
/******/ 	// expose the module cache
/******/ 	__webpack_require__.c = installedModules;
/******/
/******/ 	// define getter function for harmony exports
/******/ 	__webpack_require__.d = function(exports, name, getter) {
/******/ 		if(!__webpack_require__.o(exports, name)) {
/******/ 			Object.defineProperty(exports, name, { enumerable: true, get: getter });
/******/ 		}
/******/ 	};
/******/
/******/ 	// define __esModule on exports
/******/ 	__webpack_require__.r = function(exports) {
/******/ 		if(typeof Symbol !== 'undefined' && Symbol.toStringTag) {
/******/ 			Object.defineProperty(exports, Symbol.toStringTag, { value: 'Module' });
/******/ 		}
/******/ 		Object.defineProperty(exports, '__esModule', { value: true });
/******/ 	};
/******/
/******/ 	// create a fake namespace object
/******/ 	// mode & 1: value is a module id, require it
/******/ 	// mode & 2: merge all properties of value into the ns
/******/ 	// mode & 4: return value when already ns object
/******/ 	// mode & 8|1: behave like require
/******/ 	__webpack_require__.t = function(value, mode) {
/******/ 		if(mode & 1) value = __webpack_require__(value);
/******/ 		if(mode & 8) return value;
/******/ 		if((mode & 4) && typeof value === 'object' && value && value.__esModule) return value;
/******/ 		var ns = Object.create(null);
/******/ 		__webpack_require__.r(ns);
/******/ 		Object.defineProperty(ns, 'default', { enumerable: true, value: value });
/******/ 		if(mode & 2 && typeof value != 'string') for(var key in value) __webpack_require__.d(ns, key, function(key) { return value[key]; }.bind(null, key));
/******/ 		return ns;
/******/ 	};
/******/
/******/ 	// getDefaultExport function for compatibility with non-harmony modules
/******/ 	__webpack_require__.n = function(module) {
/******/ 		var getter = module && module.__esModule ?
/******/ 			function getDefault() { return module['default']; } :
/******/ 			function getModuleExports() { return module; };
/******/ 		__webpack_require__.d(getter, 'a', getter);
/******/ 		return getter;
/******/ 	};
/******/
/******/ 	// Object.prototype.hasOwnProperty.call
/******/ 	__webpack_require__.o = function(object, property) { return Object.prototype.hasOwnProperty.call(object, property); };
/******/
/******/ 	// __webpack_public_path__
/******/ 	__webpack_require__.p = "";
/******/
/******/
/******/ 	// Load entry module and return exports
/******/ 	return __webpack_require__(__webpack_require__.s = "./static/js/index.js");
/******/ })
/************************************************************************/
/******/ ({

/***/ "./static/js/index.js":
/*!****************************!*\
  !*** ./static/js/index.js ***!
  \****************************/
/*! no exports provided */
/***/ (function(module, exports) {

eval("throw new Error(\"Module build failed (from ./node_modules/babel-loader/lib/index.js):\\nSyntaxError: /Users/lukecarnevale/Desktop/Momentum-Projects/crop-circle/static/js/index.js: Unexpected token, expected \\\",\\\" (13:49)\\n\\n\\u001b[0m \\u001b[90m 11 | \\u001b[39m        \\u001b[33m<\\u001b[39m\\u001b[33mdiv\\u001b[39m \\u001b[36mclass\\u001b[39m\\u001b[33m=\\u001b[39m\\u001b[32m\\\"header, grid-container\\\"\\u001b[39m\\u001b[33m>\\u001b[39m\\u001b[0m\\n\\u001b[0m \\u001b[90m 12 | \\u001b[39m  \\u001b[33m<\\u001b[39m\\u001b[33mdiv\\u001b[39m \\u001b[36mclass\\u001b[39m\\u001b[33m=\\u001b[39m\\u001b[32m\\\"grid-item, text\\\"\\u001b[39m\\u001b[33m>\\u001b[39m\\u001b[0m\\n\\u001b[0m\\u001b[31m\\u001b[1m>\\u001b[22m\\u001b[39m\\u001b[90m 13 | \\u001b[39m      \\u001b[33m<\\u001b[39m\\u001b[33mh4\\u001b[39m\\u001b[33m>\\u001b[39m\\u001b[33mWelcome\\u001b[39m to your farmer\\u001b[33m-\\u001b[39mprofile\\u001b[33m,\\u001b[39m {{ user\\u001b[33m.\\u001b[39musername }}\\u001b[33m!\\u001b[39m  \\u001b[33m<\\u001b[39m\\u001b[33m/\\u001b[39m\\u001b[33mh4\\u001b[39m\\u001b[33m>\\u001b[39m\\u001b[0m\\n\\u001b[0m \\u001b[90m    | \\u001b[39m                                                 \\u001b[31m\\u001b[1m^\\u001b[22m\\u001b[39m\\u001b[0m\\n\\u001b[0m \\u001b[90m 14 | \\u001b[39m      \\u001b[33m<\\u001b[39m\\u001b[33mp\\u001b[39m\\u001b[33m>\\u001b[39m\\u001b[33mYour\\u001b[39m farmstand is currently located here\\u001b[33m!\\u001b[39m\\u001b[33m:\\u001b[39m\\u001b[33m<\\u001b[39m\\u001b[33m/\\u001b[39m\\u001b[33mp\\u001b[39m\\u001b[33m>\\u001b[39m\\u001b[0m\\n\\u001b[0m \\u001b[90m 15 | \\u001b[39m      \\u001b[33m<\\u001b[39m\\u001b[33mdiv\\u001b[39m id\\u001b[33m=\\u001b[39m\\u001b[32m'map'\\u001b[39m style\\u001b[33m=\\u001b[39m\\u001b[32m'width: 400px; height: 300px;'\\u001b[39m\\u001b[33m>\\u001b[39m\\u001b[33m<\\u001b[39m\\u001b[33m/\\u001b[39m\\u001b[33mdiv\\u001b[39m\\u001b[33m>\\u001b[39m\\u001b[0m\\n\\u001b[0m \\u001b[90m 16 | \\u001b[39m        \\u001b[33m<\\u001b[39m\\u001b[33mscript\\u001b[39m\\u001b[33m>\\u001b[39m\\u001b[0m\\n    at Object._raise (/Users/lukecarnevale/Desktop/Momentum-Projects/crop-circle/node_modules/@babel/parser/lib/index.js:757:17)\\n    at Object.raiseWithData (/Users/lukecarnevale/Desktop/Momentum-Projects/crop-circle/node_modules/@babel/parser/lib/index.js:750:17)\\n    at Object.raise (/Users/lukecarnevale/Desktop/Momentum-Projects/crop-circle/node_modules/@babel/parser/lib/index.js:744:17)\\n    at Object.unexpected (/Users/lukecarnevale/Desktop/Momentum-Projects/crop-circle/node_modules/@babel/parser/lib/index.js:8834:16)\\n    at Object.expect (/Users/lukecarnevale/Desktop/Momentum-Projects/crop-circle/node_modules/@babel/parser/lib/index.js:8820:28)\\n    at Object.parseObj (/Users/lukecarnevale/Desktop/Momentum-Projects/crop-circle/node_modules/@babel/parser/lib/index.js:10485:14)\\n    at Object.parseExprAtom (/Users/lukecarnevale/Desktop/Momentum-Projects/crop-circle/node_modules/@babel/parser/lib/index.js:10090:28)\\n    at Object.parseExprAtom (/Users/lukecarnevale/Desktop/Momentum-Projects/crop-circle/node_modules/@babel/parser/lib/index.js:4648:20)\\n    at Object.parseExprSubscripts (/Users/lukecarnevale/Desktop/Momentum-Projects/crop-circle/node_modules/@babel/parser/lib/index.js:9688:23)\\n    at Object.parseMaybeUnary (/Users/lukecarnevale/Desktop/Momentum-Projects/crop-circle/node_modules/@babel/parser/lib/index.js:9668:21)\\n    at Object.parseExprOps (/Users/lukecarnevale/Desktop/Momentum-Projects/crop-circle/node_modules/@babel/parser/lib/index.js:9538:23)\\n    at Object.parseMaybeConditional (/Users/lukecarnevale/Desktop/Momentum-Projects/crop-circle/node_modules/@babel/parser/lib/index.js:9511:23)\\n    at Object.parseMaybeAssign (/Users/lukecarnevale/Desktop/Momentum-Projects/crop-circle/node_modules/@babel/parser/lib/index.js:9466:21)\\n    at Object.parseExpression (/Users/lukecarnevale/Desktop/Momentum-Projects/crop-circle/node_modules/@babel/parser/lib/index.js:9418:23)\\n    at Object.jsxParseExpressionContainer (/Users/lukecarnevale/Desktop/Momentum-Projects/crop-circle/node_modules/@babel/parser/lib/index.js:4499:30)\\n    at Object.jsxParseElementAt (/Users/lukecarnevale/Desktop/Momentum-Projects/crop-circle/node_modules/@babel/parser/lib/index.js:4593:36)\\n    at Object.jsxParseElementAt (/Users/lukecarnevale/Desktop/Momentum-Projects/crop-circle/node_modules/@babel/parser/lib/index.js:4578:32)\\n    at Object.jsxParseElementAt (/Users/lukecarnevale/Desktop/Momentum-Projects/crop-circle/node_modules/@babel/parser/lib/index.js:4578:32)\\n    at Object.jsxParseElementAt (/Users/lukecarnevale/Desktop/Momentum-Projects/crop-circle/node_modules/@babel/parser/lib/index.js:4578:32)\\n    at Object.jsxParseElement (/Users/lukecarnevale/Desktop/Momentum-Projects/crop-circle/node_modules/@babel/parser/lib/index.js:4636:17)\\n    at Object.parseExprAtom (/Users/lukecarnevale/Desktop/Momentum-Projects/crop-circle/node_modules/@babel/parser/lib/index.js:4643:19)\\n    at Object.parseExprSubscripts (/Users/lukecarnevale/Desktop/Momentum-Projects/crop-circle/node_modules/@babel/parser/lib/index.js:9688:23)\\n    at Object.parseMaybeUnary (/Users/lukecarnevale/Desktop/Momentum-Projects/crop-circle/node_modules/@babel/parser/lib/index.js:9668:21)\\n    at Object.parseExprOps (/Users/lukecarnevale/Desktop/Momentum-Projects/crop-circle/node_modules/@babel/parser/lib/index.js:9538:23)\\n    at Object.parseMaybeConditional (/Users/lukecarnevale/Desktop/Momentum-Projects/crop-circle/node_modules/@babel/parser/lib/index.js:9511:23)\\n    at Object.parseMaybeAssign (/Users/lukecarnevale/Desktop/Momentum-Projects/crop-circle/node_modules/@babel/parser/lib/index.js:9466:21)\\n    at Object.parseParenAndDistinguishExpression (/Users/lukecarnevale/Desktop/Momentum-Projects/crop-circle/node_modules/@babel/parser/lib/index.js:10313:28)\\n    at Object.parseExprAtom (/Users/lukecarnevale/Desktop/Momentum-Projects/crop-circle/node_modules/@babel/parser/lib/index.js:10042:21)\\n    at Object.parseExprAtom (/Users/lukecarnevale/Desktop/Momentum-Projects/crop-circle/node_modules/@babel/parser/lib/index.js:4648:20)\\n    at Object.parseExprSubscripts (/Users/lukecarnevale/Desktop/Momentum-Projects/crop-circle/node_modules/@babel/parser/lib/index.js:9688:23)\");\n\n//# sourceURL=webpack:///./static/js/index.js?");

/***/ })

/******/ });