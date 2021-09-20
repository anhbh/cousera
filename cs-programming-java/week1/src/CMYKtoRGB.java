public class CMYKtoRGB {
    public static void main (String[] args) {
        double cyan     = Double.parseDouble(args[0]);
        double magenta  = Double.parseDouble(args[1]);
        double yellow   = Double.parseDouble(args[2]);
        double black    = Double.parseDouble(args[3]);

        int red, green, blue, white;

        white = (int) (1 - black);
        red = (int) (255 * white * (1 - cyan));
        green = (int) (255 * white * (1 - magenta));
        blue = (int) (255 * white * (1 - yellow));

        System.out.println("red \t= "+red);
        System.out.println("green\t= "+green);
        System.out.println("blue\t= "+blue);
        return;
    }
}
