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

eval("throw new Error(\"Module build failed (from ./node_modules/babel-loader/lib/index.js):\\nSyntaxError: /Users/lukecarnevale/Desktop/Momentum-Projects/crop-circle/static/js/index.js: Identifier 'App' has already been declared (6:6)\\n\\n\\u001b[0m \\u001b[90m 4 | \\u001b[39m\\u001b[90m// import './styles.css'\\u001b[39m\\u001b[0m\\n\\u001b[0m \\u001b[90m 5 | \\u001b[39m\\u001b[0m\\n\\u001b[0m\\u001b[31m\\u001b[1m>\\u001b[22m\\u001b[39m\\u001b[90m 6 | \\u001b[39m\\u001b[36mclass\\u001b[39m \\u001b[33mApp\\u001b[39m \\u001b[36mextends\\u001b[39m \\u001b[33mReact\\u001b[39m\\u001b[33m.\\u001b[39m\\u001b[33mComponent\\u001b[39m {\\u001b[0m\\n\\u001b[0m \\u001b[90m   | \\u001b[39m      \\u001b[31m\\u001b[1m^\\u001b[22m\\u001b[39m\\u001b[0m\\n\\u001b[0m \\u001b[90m 7 | \\u001b[39m  render () {\\u001b[0m\\n\\u001b[0m \\u001b[90m 8 | \\u001b[39m    \\u001b[36mreturn\\u001b[39m (\\u001b[0m\\n\\u001b[0m \\u001b[90m 9 | \\u001b[39m      \\u001b[33m<\\u001b[39m\\u001b[33mdiv\\u001b[39m\\u001b[33m>\\u001b[39m\\u001b[0m\\n    at Object._raise (/Users/lukecarnevale/Desktop/Momentum-Projects/crop-circle/node_modules/@babel/parser/lib/index.js:757:17)\\n    at Object.raiseWithData (/Users/lukecarnevale/Desktop/Momentum-Projects/crop-circle/node_modules/@babel/parser/lib/index.js:750:17)\\n    at Object.raise (/Users/lukecarnevale/Desktop/Momentum-Projects/crop-circle/node_modules/@babel/parser/lib/index.js:744:17)\\n    at ScopeHandler.checkRedeclarationInScope (/Users/lukecarnevale/Desktop/Momentum-Projects/crop-circle/node_modules/@babel/parser/lib/index.js:4803:12)\\n    at ScopeHandler.declareName (/Users/lukecarnevale/Desktop/Momentum-Projects/crop-circle/node_modules/@babel/parser/lib/index.js:4769:12)\\n    at Object.checkLVal (/Users/lukecarnevale/Desktop/Momentum-Projects/crop-circle/node_modules/@babel/parser/lib/index.js:9288:22)\\n    at Object.parseClassId (/Users/lukecarnevale/Desktop/Momentum-Projects/crop-circle/node_modules/@babel/parser/lib/index.js:12264:14)\\n    at Object.parseClass (/Users/lukecarnevale/Desktop/Momentum-Projects/crop-circle/node_modules/@babel/parser/lib/index.js:11963:10)\\n    at Object.parseStatementContent (/Users/lukecarnevale/Desktop/Momentum-Projects/crop-circle/node_modules/@babel/parser/lib/index.js:11252:21)\\n    at Object.parseStatement (/Users/lukecarnevale/Desktop/Momentum-Projects/crop-circle/node_modules/@babel/parser/lib/index.js:11210:17)\\n    at Object.parseBlockOrModuleBlockBody (/Users/lukecarnevale/Desktop/Momentum-Projects/crop-circle/node_modules/@babel/parser/lib/index.js:11785:25)\\n    at Object.parseBlockBody (/Users/lukecarnevale/Desktop/Momentum-Projects/crop-circle/node_modules/@babel/parser/lib/index.js:11771:10)\\n    at Object.parseTopLevel (/Users/lukecarnevale/Desktop/Momentum-Projects/crop-circle/node_modules/@babel/parser/lib/index.js:11141:10)\\n    at Object.parse (/Users/lukecarnevale/Desktop/Momentum-Projects/crop-circle/node_modules/@babel/parser/lib/index.js:12843:10)\\n    at parse (/Users/lukecarnevale/Desktop/Momentum-Projects/crop-circle/node_modules/@babel/parser/lib/index.js:12896:38)\\n    at parser (/Users/lukecarnevale/Desktop/Momentum-Projects/crop-circle/node_modules/@babel/core/lib/parser/index.js:54:34)\\n    at parser.next (<anonymous>)\\n    at normalizeFile (/Users/lukecarnevale/Desktop/Momentum-Projects/crop-circle/node_modules/@babel/core/lib/transformation/normalize-file.js:93:38)\\n    at normalizeFile.next (<anonymous>)\\n    at run (/Users/lukecarnevale/Desktop/Momentum-Projects/crop-circle/node_modules/@babel/core/lib/transformation/index.js:31:50)\\n    at run.next (<anonymous>)\\n    at Function.transform (/Users/lukecarnevale/Desktop/Momentum-Projects/crop-circle/node_modules/@babel/core/lib/transform.js:27:41)\\n    at transform.next (<anonymous>)\\n    at step (/Users/lukecarnevale/Desktop/Momentum-Projects/crop-circle/node_modules/gensync/index.js:254:32)\\n    at /Users/lukecarnevale/Desktop/Momentum-Projects/crop-circle/node_modules/gensync/index.js:266:13\\n    at async.call.result.err.err (/Users/lukecarnevale/Desktop/Momentum-Projects/crop-circle/node_modules/gensync/index.js:216:11)\");\n\n//# sourceURL=webpack:///./static/js/index.js?");

/***/ })

/******/ });