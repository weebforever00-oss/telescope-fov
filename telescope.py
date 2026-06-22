#!/usr/bin/env python3
"""Telescope field of view calculator."""

def fov_degrees(aperture_mm, focal_length_mm, eyepiece_mm):
    """Calculate FOV and magnification."""
    mag = focal_length_mm / eyepiece_mm
    fov = 57.3 * eyepiece_mm / focal_length_mm  # approximate
    return fov, mag

def limiting_magnitude(aperture_mm):
    """Theoretical limiting magnitude."""
    return 2.5 + 5 * (aperture_mm / 25.4)  # simplified

def resolution_arcsec(aperture_mm):
    """Dawes limit in arcseconds."""
    return 116 / aperture_mm

if __name__ == "__main__":
    scopes = [("80mm f/5", 80, 400), ("6in f/8", 152, 1219), ("10in f/4.7", 254, 1200)]
    eyepieces = [6, 10, 25, 40]
    print("Telescope FOV Calculator")
    for name, ap, fl in scopes:
        print(f"\n  {name}:")
        for ep in eyepieces:
            fov, mag = fov_degrees(ap, fl, ep)
            lm = limiting_magnitude(ap)
            print(f"    {ep}mm: {mag:.0f}x, FOV={fov:.1f}, lim_mag={lm:.1f}")\n