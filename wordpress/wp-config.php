<?php
/**
 * The base configuration for WordPress
 *
 * The wp-config.php creation script uses this file during the
 * installation. You don't have to use the web site, you can
 * copy this file to "wp-config.php" and fill in the values.
 *
 * This file contains the following configurations:
 *
 * * MySQL settings
 * * Secret keys
 * * Database table prefix
 * * ABSPATH
 *
 * @link https://codex.wordpress.org/Editing_wp-config.php
 *
 * @package WordPress
 */

// ** MySQL settings - You can get this info from your web host ** //
/** The name of the database for WordPress */
define('DB_NAME', 'apolloDB');

/** MySQL database username */
define('DB_USER', 'root');

/** MySQL database password */
define('DB_PASSWORD', 'root');

/** MySQL hostname */
define('DB_HOST', 'localhost');

/** Database Charset to use in creating database tables. */
define('DB_CHARSET', 'utf8mb4');

/** The Database Collate type. Don't change this if in doubt. */
define('DB_COLLATE', '');

/**#@+
 * Authentication Unique Keys and Salts.
 *
 * Change these to different unique phrases!
 * You can generate these using the {@link https://api.wordpress.org/secret-key/1.1/salt/ WordPress.org secret-key service}
 * You can change these at any point in time to invalidate all existing cookies. This will force all users to have to log in again.
 *
 * @since 2.6.0
 */
define('AUTH_KEY',         '4~#S>~Y+^kU^_9i.5{-;g*R<6VCU>mckqX/Gc!6#gj6JdYtE/?QtM V6/B/_~es)');
define('SECURE_AUTH_KEY',  '}<^)Ce,+4+<ZQ7E^H/@J!.Mq<W[47/p4 U#Q>cu3[H<eTEHz%# c)W?tAV=A=cOS');
define('LOGGED_IN_KEY',    'r~{O9M*8je<P|)TV4lv+a6=Apdf(58rrbDg &.|O$~3H8F5)/U=$Xve0FC,+7B&|');
define('NONCE_KEY',        'dSS#b@?H2y^gw LFR6U)!6B7;.Y86B`MAw~Ed9<CsFN3_kHk29:wd$KQnsu0?77C');
define('AUTH_SALT',        'N=bVWE9[Z~]r+2n8hiso7N?z=.dyQ^64GPbt/zMDvG<7fz8.eF|V2OAdhp-,9KWk');
define('SECURE_AUTH_SALT', ';29.B<JPepOPNX@2~vZv[LXD(4u~%W]ZZhwpL=-c=vkUp/a>J-&X0;f8,p>~`m=f');
define('LOGGED_IN_SALT',   '+Ii}^fQ,k{$Fs)i5%mEoQ1{V_,{+uOjI9oo0F!vFu5QP<ZxM/z1H$V L3MRg$dvm');
define('NONCE_SALT',       'K=LXGnNXMZPK+$Z9f,]f8ID$n^Jy[$I~Ds3J|^{U@9?e#_uVCQC/=?e_!W i?O>[');

/**#@-*/

/**
 * WordPress Database Table prefix.
 *
 * You can have multiple installations in one database if you give each
 * a unique prefix. Only numbers, letters, and underscores please!
 */
$table_prefix  = 'wp_';

/**
 * For developers: WordPress debugging mode.
 *
 * Change this to true to enable the display of notices during development.
 * It is strongly recommended that plugin and theme developers use WP_DEBUG
 * in their development environments.
 *
 * For information on other constants that can be used for debugging,
 * visit the Codex.
 *
 * @link https://codex.wordpress.org/Debugging_in_WordPress
 */
define('WP_DEBUG', false);

/* That's all, stop editing! Happy blogging. */

/** Absolute path to the WordPress directory. */
if ( !defined('ABSPATH') )
	define('ABSPATH', dirname(__FILE__) . '/');

/** Sets up WordPress vars and included files. */
require_once(ABSPATH . 'wp-settings.php');
