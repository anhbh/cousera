public class CMYKtoRGB {
    public static void main(String[] args) {
        double cyan     = Double.parseDouble(args[0]);
        double magenta  = Double.parseDouble(args[1]);
        double yellow   = Double.parseDouble(args[2]);
        double black    = Double.parseDouble(args[3]);

        double red, green, blue, white;

        white = 1 - black;
        red = 255 * white * (1 - cyan);
        green = 255 * white * (1 - magenta);
        blue = 255 * white * (1 - yellow);

        System.out.println("red \t= "+Math.round(red));
        System.out.println("green\t= "+Math.round(green));
        System.out.println("blue\t= "+Math.round(blue));
        return;
    }
}
