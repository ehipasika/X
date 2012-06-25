#
# The XBUILD configuration file.
#
# (c) 2012 The XTK Developers <dev@goXTK.com>
#

import os
import sys
import tempfile


# STRINGS
SOFTWARE = 'The X Toolkit'
SOFTWARE_SHORT = 'XTK'
SOFTWARE_DESCRIPTION = 'XTK is a WebGL framework providing an easy-to-use API to visualize scientific data on the web.<br>No background or knowledge in Computer Graphics is required.'
SOFTWARE_HOMEPAGE = 'http://goXTK.com'

NAMESPACE = 'X'

LICENSE_HEADER = '''/*
 * 
 *                  xxxxxxx      xxxxxxx
 *                   x:::::x    x:::::x 
 *                    x:::::x  x:::::x  
 *                     x:::::xx:::::x   
 *                      x::::::::::x    
 *                       x::::::::x     
 *                       x::::::::x     
 *                      x::::::::::x    
 *                     x:::::xx:::::x   
 *                    x:::::x  x:::::x  
 *                   x:::::x    x:::::x 
 *              THE xxxxxxx      xxxxxxx TOOLKIT
 *                    
 *                  http://www.goXTK.com
 *                   
 * Copyright (c) 2012 The X Toolkit Developers <dev@goXTK.com>
 *                   
 *    The X Toolkit (XTK) is licensed under the MIT License:
 *      http://www.opensource.org/licenses/mit-license.php
 * 
 *      "Free software" is a matter of liberty, not price.
 *      "Free" as in "free speech", not as in "free beer".
 *                                         - Richard M. Stallman
 * 
 * FUELED BY:
 *  - the wonderful Constructive Solid Geometry library by Evan Wallace (http://madebyevan.com)
 *    LICENSE: https://raw.github.com/xtk/X/master/lib/csg/LICENSE
 *
 *  - parts of the Google Closure Library (http://code.google.com/closure/library)
 *    LICENSE: https://raw.github.com/xtk/X/master/lib/closure-library/LICENSE
 * 
 *  - the JSXCompressor library (http://jsxgraph.uni-bayreuth.de/wp/jsxcompressor/)
 *    LICENSE: https://raw.github.com/xtk/X/master/lib/JXG/LICENSE
 *
 * MORE CREDITS: https://raw.github.com/xtk/X/master/LICENSE
 *
 */'''


# PATHS
EXCLUDES_PATH = ['lib', 'testing', 'deps', 'utils']
INCLUDES_PATH = ['csg', 'JXG'] # force inclusion of sub folders in an excluded directory for dependency generation

REPOSITORY_URL = 'https://github.com/xtk/X/blob/master/'

CDASH_SUBMIT_URL = 'http://x.babymri.org/cdash/submit.php?project=' + SOFTWARE_SHORT

XBUILD_PATH = os.path.abspath( os.path.dirname( sys.argv[0] ) )
SOFTWARE_PATH = os.path.normpath( XBUILD_PATH + os.sep + '..' + os.sep )

CLOSURELIBRARY_PATH = os.path.normpath( os.path.join( SOFTWARE_PATH, 'lib/closure-library/closure/' ) )
CLOSURELIBRARY_PYTHON_PATH = os.path.normpath( os.path.join( CLOSURELIBRARY_PATH, 'bin/build/' ) )
CLOSUREBUILDER_PATH = os.path.normpath( os.path.join( CLOSURELIBRARY_PYTHON_PATH, 'closurebuilder.py' ) )
CLOSUREDEPSWRITER_PATH = os.path.normpath( os.path.join( CLOSURELIBRARY_PYTHON_PATH, 'depswriter.py' ) )
CLOSURECOMPILER_PATH = os.path.normpath( os.path.join( SOFTWARE_PATH, 'lib/closure-library/compiler-latest/compiler.jar' ) )
CLOSUREGOOGBASE_PATH = os.path.normpath( os.path.join( CLOSURELIBRARY_PATH, 'goog/base.js' ) )

DOC_TEMPLATES_PATH = os.path.normpath( os.path.join( XBUILD_PATH, '_core', 'templates/' ) )

BUILD_OUTPUT_PATH = os.path.normpath( os.path.join( XBUILD_PATH , SOFTWARE_SHORT.lower() + '.js' ) )
DEPS_OUTPUT_PATH = os.path.normpath( os.path.join( SOFTWARE_PATH , SOFTWARE_SHORT.lower() + '-deps.js' ) )
DOC_OUTPUT_PATH = os.path.normpath( os.path.join( SOFTWARE_PATH , 'doc/' ) )

TEMP_PATH = tempfile.gettempdir()
